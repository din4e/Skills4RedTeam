# Skills4RedTeam

面向红队的Skills集合。

## 简介

本仓库收录了面向 Claude 技能系统的安全技能合集。每个技能是一个结构化的 `SKILL.md` 文件，为 Claude 注入针对特定攻击面的专业方法论 —— 从 SQL 注入到 Shellcode 编写，从 EDR 规避到漏洞利用开发、逆向工程、代码审计。

仓库同时收录社区开源的优秀安全技能推荐，形成覆盖攻击性安全、防御审计、漏洞研究等多领域的完整技能生态。

## 社区技能推荐

以下为社区开源的优秀安全技能，按 Star 数降序排列，数据更新于 2026-08-01。

### 攻防渗透

| 技能 | Star | 更新时间 | 说明 | 仓库 |
| --- | --- | --- | --- | --- |
| `raptor` | ![GitHub Repo stars](https://img.shields.io/github/stars/gadievron/raptor?style=social) | 2026-08-01 | 将 Claude Code 转为通用攻防安全 agent，覆盖侦察 → 入侵 → 横向移动 → 后渗透全流程，自动编排攻击链（疑为 GitHub Trending 榜首的全自动 AI 渗透测试员） | [gadievron/raptor](https://github.com/gadievron/raptor) |
| `Claude-BugHunter` | ![GitHub Repo stars](https://img.shields.io/github/stars/elementalsouls/Claude-BugHunter?style=social) | 2026-07-31 | 红队 / 外部渗透漏洞挖掘技能包 —— 82 个 skill + 15 个 slash command，聚焦 bug bounty 与红队行动方法论 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) |
| `Claude-Red` | ![GitHub Repo stars](https://img.shields.io/github/stars/SnailSploit/Claude-Red?style=social) | 2026-04-15 | 37 个即插即用的攻击性安全技能 —— Web 攻击（SQLi/XSS/SSRF/SSTI/XXE）、Shellcode 编写、EDR 规避、漏洞利用开发、红队行动、OSINT、模糊测试等 | [SnailSploit/Claude-Red](https://github.com/SnailSploit/Claude-Red) |
| `Claude-OSINT` | ![GitHub Repo stars](https://img.shields.io/github/stars/elementalsouls/Claude-OSINT?style=social) | 2026-06-08 | OSINT / 侦察技能对 —— 90+ 侦察模块、48 个 secret-regex 模式、80+ Google dorks、9 个侦察引擎 | [elementalsouls/Claude-OSINT](https://github.com/elementalsouls/Claude-OSINT) |
| `iothackbot` | ![GitHub Repo stars](https://img.shields.io/github/stars/BrownFineSecurity/iothackbot?style=social) | 2026-06-01 | IoT 渗透测试技能集 + 混合 IoT pentest 工具链（固件分析、硬件接口、无线协议等） | [BrownFineSecurity/iothackbot](https://github.com/BrownFineSecurity/iothackbot) |
| `communitytools` | ![GitHub Repo stars](https://img.shields.io/github/stars/transilienceai/communitytools?style=social) | 2026-07-29 | 面向 AI 驱动渗透测试的开源 skills / agents / slash commands 集合 | [transilienceai/communitytools](https://github.com/transilienceai/communitytools) |
| `cti-expert` | ![GitHub Repo stars](https://img.shields.io/github/stars/7onez/cti-expert?style=social) | 2026-08-01 | 网络威胁情报（CTI）& OSINT 分析技能 —— 67+ commands，IOC 提取、威胁画像、情报收集与关联 | [7onez/cti-expert](https://github.com/7onez/cti-expert) |
| `awesome-skills-security` | ![GitHub Repo stars](https://img.shields.io/github/stars/Eyadkelleh/awesome-skills-security?style=social) | 2026-06-08 | 从 SecLists 打包的安全测试工具包，提供 wordlists、injection payloads、patterns、webshells 等，即插即用，适合 pentest、CTF、bug bounty | [Eyadkelleh/awesome-skills-security](https://github.com/Eyadkelleh/awesome-skills-security) |
| `pentest-skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/crazyMarky/pentest-skills?style=social) | 2026-06-04 | 模块化渗透测试技能 —— 自然语言驱动专业级 pentest（信息收集 → 漏洞利用 → 后渗透），支持 Claude Code / Gemini CLI | [crazyMarky/pentest-skills](https://github.com/crazyMarky/pentest-skills) |
| `red-run` | ![GitHub Repo stars](https://img.shields.io/github/stars/blacklanternsecurity/red-run?style=social) | 2026-04-01 | 攻击性安全工具包，结合 Skills + MCP Servers + Agent Teams，实现 recon → initial access → lateral movement → privilege escalation → post-access 完整红队流程路由 | [blacklanternsecurity/red-run](https://github.com/blacklanternsecurity/red-run) |
| `Claude-Code-CyberSecurity-Skill` | ![GitHub Repo stars](https://img.shields.io/github/stars/Masriyan/Claude-Code-CyberSecurity-Skill?style=social) | 2026-02-27 | 15 个 Claude Code 安全技能，覆盖攻击性安全、防御运营、逆向工程、威胁狩猎、CSOC 自动化、红队行动、密码分析等，较为全面的 Cybersecurity 技能集合 | [Masriyan/Claude-Code-CyberSecurity-Skill](https://github.com/Masriyan/Claude-Code-CyberSecurity-Skill) |
| `Black-cat` | ![GitHub Repo stars](https://img.shields.io/github/stars/0rangec3t/Black-cat?style=social) | 2026-07-31 | 假设-证据驱动的红队技能（Hypothesis-Driven Cognitive Architecture）—— 区别于流水线式 pentest skill，采用状态机设计（RECON ⇄ ENUMERATE ⇄ VALIDATE），失败与新发现可回溯重启早期阶段；覆盖信息收集、Web 渗透、内网横向、云安全、EDR 规避、数据库利用、逆向工程等 7 个 technique | [0rangec3t/Black-cat](https://github.com/0rangec3t/Black-cat) |

### 逆向工程

| 技能 | Star | 更新时间 | 说明 | 仓库 |
| --- | --- | --- | --- | --- |
| `android-reverse-engineering` | ![GitHub Repo stars](https://img.shields.io/github/stars/SimoneAvogadro/android-reverse-engineering-skill?style=social) | 2026-04-27 | Android APK/XAPK/JAR/AAR 逆向 —— jadx 反编译、Retrofit/OkHttp API 提取、调用流追踪、ProGuard 混淆分析 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) |
| `reverse-engineering` | ![GitHub Repo stars](https://img.shields.io/github/stars/P4nda0s/reverse-skills?style=social) | 2026-04-21 | 二进制逆向工程 —— 配合 IDA-NO-MCP 导出反编译结果，分析函数符号、重建数据结构（rev-symbol / rev-struct） | [P4nda0s/reverse-skills](https://github.com/P4nda0s/reverse-skills) |
| `ai-mobile-reverse-skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/Fausto-404/ai-mobile-reverse-skills?style=social) | 2026-04-28 | 移动安全分析 6 阶段总控 —— APK 静态侦察、流量与代码对齐、SO/JNI 深度分析、加密与漏洞综合分析、验证设计与报告交付，支持 JADX/Burp/Yakit/IDA/Ghidra MCP | [Fausto-404/ai-mobile-reverse-skills](https://github.com/Fausto-404/ai-mobile-reverse-skills) |
| `android-reverse-engineering-claude-skill` | ![GitHub Repo stars](https://img.shields.io/github/stars/incogbyte/android-reverse-engineering-claude-skill?style=social) | 2026-04-22 | Android 逆向自动化技能 —— APK/XAPK/AAB/DEX/JAR/AAR 反编译（jadx + Fernflower）、Retrofit/OkHttp HTTP 端点提取 | [incogbyte/android-reverse-engineering-claude-skill](https://github.com/incogbyte/android-reverse-engineering-claude-skill) |

### 代码审计

| 技能 | Star | 更新时间 | 说明 | 仓库 |
| --- | --- | --- | --- | --- |
| `VibeSec-Skill` | ![GitHub Repo stars](https://img.shields.io/github/stars/BehiSecc/VibeSec-Skill?style=social) | 2026-02-17 | 安全优先代码审查 —— 以漏洞猎手视角审视代码，捕获 Web 应用常见漏洞（OWASP Top 10），防御性安全辅助 | [BehiSecc/VibeSec-Skill](https://github.com/BehiSecc/VibeSec-Skill) |
| `java-audit-skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/RuoJi6/java-audit-skills?style=social) | 2026-04-29 | Java Web 源码安全审计 —— 路由提取、SQL 注入/XXE/文件上传/鉴权绕过等多维度自动化审计，模拟资深安全研究员思维 | [RuoJi6/java-audit-skills](https://github.com/RuoJi6/java-audit-skills) |
| `code-audit` | ![GitHub Repo stars](https://img.shields.io/github/stars/3stoneBrother/code-audit?style=social) | 2026-02-13 | 通用代码审计 —— 支持 55+ 漏洞类型，双轨审计模型（自动化 + 专家模式），覆盖 Java/Python/Go/PHP/JS/C 等多语言 | [3stoneBrother/code-audit](https://github.com/3stoneBrother/code-audit) |
| `PHP_AUDIT_SKILLS` | ![GitHub Repo stars](https://img.shields.io/github/stars/yunmengya/PHP_AUDIT_SKILLS?style=social) | 2026-04-09 | PHP 代码审计 —— 基于 Agent Teams 多智能体协作，静态分析 + 动态追踪 + AI 辅助三重审计，覆盖 21 种漏洞类型 | [yunmengya/PHP_AUDIT_SKILLS](https://github.com/yunmengya/PHP_AUDIT_SKILLS) |

### 漏洞知识库

| 技能 | Star | 更新时间 | 说明 | 仓库 |
| --- | --- | --- | --- | --- |
| `wooyun-legacy` | ![GitHub Repo stars](https://img.shields.io/github/stars/tanweai/wooyun-legacy?style=social) | 2026-03-08 | WooYun 漏洞知识库 —— 88,636 个真实漏洞案例（SQL 注入 27%、命令执行 19%、XSS 11% 等 15 种类型），86MB 精炼安全方法论 | [tanweai/wooyun-legacy](https://github.com/tanweai/wooyun-legacy) |

### 综合安全仓库

| 技能 | Star | 更新时间 | 说明 | 仓库 |
| --- | --- | --- | --- | --- |
| `claude-skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/alirezarezvani/claude-skills?style=social) | 2026-04-28 | 232+ 技能大型集合，包含多个安全相关子技能：senior-security（威胁建模/渗透测试/OWASP）、ai-security（Prompt 注入检测/模型安全）、cloud-security（CSPM 云安全）、security-pen-testing 等，推荐作为技能库底座 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) |
| `skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/trailofbits/skills?style=social) | 2026-04-29 | Trail of Bits 出品，17+ 安全研究技能 —— 漏洞检测、差分代码审查、审计上下文构建、修复验证，专注安全研究、漏洞检测与审计工作流，质量较高 | [trailofbits/skills](https://github.com/trailofbits/skills) |
| `SecSkills` | ![GitHub Repo stars](https://img.shields.io/github/stars/DaoYiSec/SecSkills?style=social) | 2026-04-21 | 刀义安全出品，53 个安全技能索引，覆盖代码审计、渗透测试、JS 逆向、CTF、红蓝对抗、移动安全、应急响应等 16 个分类 | [DaoYiSec/SecSkills](https://github.com/DaoYiSec/SecSkills) |
| `openclaw-sec-skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/Batman0506/openclaw-sec-skills?style=social) | 2026-04-22 | OpenClaw 社区安全技能大全，150+ 技能索引，涵盖代码审计、渗透测试、逆向工程、CTF、威胁建模、移动安全、应急响应、安全工具 8 大领域 | [Batman0506/openclaw-sec-skills](https://github.com/Batman0506/openclaw-sec-skills) |

## 许可证

MIT 许可证 —— 详见 [LICENSE](LICENSE)。
