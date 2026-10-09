#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每日刷新 README.md 社区技能表格。

- 调用 GitHub API 获取各仓库的 stargazers_count 与 pushed_at
- 每个分类表格内按 Star 数降序重排（稳定排序，Star 相同保持原顺序）
- 「更新时间」列写为仓库最近一次 push 的日期（UTC+8）
- 顶部「数据更新于」刷新为当天日期（UTC+8）
- 仓库已删除（404/410）时保留行，排到表尾且不改日期

用法:
    python scripts/update_readme.py [--dry-run]

凭证: 依次读取环境变量 GITHUB_TOKEN / GH_TOKEN；无凭证时走匿名限流（60 次/小时）。
"""

import argparse
import difflib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

TZ_CN = timezone(timedelta(hours=8))
README_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "README.md")

GITHUB_LINK_RE = re.compile(r"\[[^\]]*\]\(https://github\.com/([^/\s)]+/[^/\s)]+)\)")
DATA_DATE_RE = re.compile(r"(数据更新于 )(\d{4}-\d{2}-\d{2})")


def die(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def api_get(url, token):
    """GET 一个 GitHub API 地址，带重试。返回 (status, json)。"""
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "Skills4RedTeam-readme-updater",
    })
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    last_err = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.status, json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):  # 仓库已删除/不可见，不重试
                return e.code, None
            last_err = e
        except urllib.error.URLError as e:
            last_err = e
        time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"请求 {url} 失败: {last_err}")


def check_rate_limit(token, need):
    """匿名调用 /rate_limit（不计入配额），配额不足则报错退出。"""
    _, data = api_get("https://api.github.com/rate_limit", token)
    remaining = data["resources"]["core"]["remaining"]
    print(f"API 配额剩余: {remaining}（本次需要 {need}）")
    if remaining < need:
        die("GitHub API 配额不足，请设置 GITHUB_TOKEN 后重试")


def fetch_repo(repo, token):
    """返回 (stars, pushed_date)。stars=None 表示仓库已删除。"""
    status, data = api_get(f"https://api.github.com/repos/{repo}", token)
    if status in (404, 410):
        return None, None
    stars = data.get("stargazers_count")
    pushed = data.get("pushed_at")
    pushed_date = datetime.strptime(pushed, "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=timezone.utc).astimezone(TZ_CN).date().isoformat() if pushed else None
    return stars, pushed_date


def parse_readme(lines):
    """定位所有「社区技能推荐」下的表格。

    返回 tables: [{header_end, rows: [行号]}]，行号指向 lines 中的数据行
    （跳过表头与 --- 分隔行）。
    """
    tables, i, n = [], 0, len(lines)
    while i < n:
        if not lines[i].lstrip().startswith("|"):
            i += 1
            continue
        block_start = i
        while i < n and lines[i].lstrip().startswith("|"):
            i += 1
        block = lines[block_start:i]
        # 需要: 表头 + --- 分隔行 + 至少一行数据，且表头含「更新时间」列
        if len(block) >= 3 and "更新时间" in block[0] and set(block[1].replace("|", "").strip()) <= {"-", " ", ":"}:
            tables.append({"start": block_start, "rows": list(range(block_start + 2, i))})
    return tables


def row_repo(line):
    """从数据行最后一个单元格提取 owner/repo。"""
    parts = line.split("|")
    if len(parts) < 6:  # 行首尾空串 + 5 列
        return None
    m = GITHUB_LINK_RE.search(parts[-2])
    return m.group(1) if m else None


def set_date_cell(line, new_date):
    parts = line.split("|")
    parts[3] = f" {new_date} "
    return "|".join(parts)


def main():
    ap = argparse.ArgumentParser(description="刷新 README 社区技能表格")
    ap.add_argument("--dry-run", action="store_true", help="只打印 diff，不写回文件")
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

    with open(README_PATH, "r", encoding="utf-8", newline="") as f:
        original = f.read()
    lines = original.splitlines(keepends=True)

    tables = parse_readme(lines)
    if not tables:
        die("未在 README.md 中找到任何表格")

    # 收集所有数据行 -> 仓库，去重后批量拉取
    row_repos = {}
    for t in tables:
        for idx in t["rows"]:
            repo = row_repo(lines[idx])
            if repo:
                row_repos[idx] = repo
    all_repos = sorted(set(row_repos.values()))
    print(f"共发现 {len(all_repos)} 个仓库，{len(tables)} 个表格")

    check_rate_limit(token, len(all_repos))

    info = {}
    for repo in all_repos:
        stars, pushed_date = fetch_repo(repo, token)
        info[repo] = {"stars": stars, "date": pushed_date}
        flag = " [已删除]" if stars is None else ""
        print(f"  {repo}: {stars} stars, pushed {pushed_date}{flag}")

    new_lines = lines[:]
    date_changed, gone = [], []

    for t in tables:
        # 组装 (行号, 排序键)，404 仓库排在最后
        indexed = []
        for pos, idx in enumerate(t["rows"]):
            repo = row_repos.get(idx)
            if repo and repo in info:
                stars = info[repo]["stars"]
                key = 1 if stars is None else -stars  # 降序；None(已删除) -> 1 排最后
            else:
                key = 0  # 未识别出仓库的行不动（理论上不存在）
            indexed.append((key, pos, idx))

        indexed.sort(key=lambda x: (x[0], x[1]))
        sorted_rows = [idx for _, _, idx in indexed]

        for new_pos, idx in enumerate(sorted_rows):
            target = t["rows"][new_pos]
            line = lines[idx]
            repo = row_repos.get(idx)
            if repo and info[repo]["date"]:
                new_line = set_date_cell(line, info[repo]["date"])
                if new_line != line:
                    date_changed.append(repo)
                line = new_line
            if repo and info[repo]["stars"] is None:
                gone.append(repo)
            new_lines[target] = line

    # 刷新顶部「数据更新于」日期
    today = datetime.now(TZ_CN).date().isoformat()
    new_text = "".join(new_lines)
    new_text = DATA_DATE_RE.sub(lambda m: m.group(1) + today, new_text, count=1)

    if new_text == original:
        print("无变化，README 已是最新")
        return

    print(f"\n更新时间列变更: {len(date_changed)} 个仓库")
    if gone:
        print(f"警告 - 以下仓库已删除(保留行, 排至表尾): {', '.join(sorted(set(gone)))}")

    if args.dry_run:
        diff = difflib.unified_diff(
            original.splitlines(), new_text.splitlines(),
            fromfile="README.md", tofile="README.md (new)", lineterm="")
        print("\n".join(list(diff)[:80]))
        return

    with open(README_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(new_text)
    print(f"已写回 README.md（数据更新于 {today}）")


if __name__ == "__main__":
    main()
