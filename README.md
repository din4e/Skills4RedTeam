# Skills4RedTeam

面向红队的Skills集合。

## 简介

本仓库收录了面向 Claude 技能系统的安全技能合集。每个技能是一个结构化的 `SKILL.md` 文件，为 Claude 注入针对特定攻击面的专业方法论 —— 从 SQL 注入到 Shellcode 编写，从 EDR 规避到漏洞利用开发、逆向工程、代码审计。

仓库同时收录社区开源的优秀安全技能推荐，形成覆盖攻击性安全、防御审计、漏洞研究等多领域的完整技能生态。

## 社区技能推荐

以下为社区开源的优秀安全技能，按 Star 数降序排列，数据更新于 2026-09-05。

### 攻防渗透

| 技能 | Star | 更新时间 | 说明 | 仓库 |
| --- | --- | --- | --- | --- |
| `Claude-BugHunter` | ![GitHub Repo stars](https://img.shields.io/github/stars/elementalsouls/Claude-BugHunter?style=social) | 2026-09-04 | 红队 / 外部渗透漏洞挖掘技能包 —— 82 个 skill + 15 个 slash command + 681 份已披露报告模式（覆盖 24 类核心漏洞）+ 企业身份与基础设施攻击矩阵，聚焦 bug bounty 与红队行动方法论 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) |
| `raptor` | ![GitHub Repo stars](https://img.shields.io/github/stars/gadievron/raptor?style=social) | 2026-09-01 | 将 Claude Code 转为通用攻防安全 agent，覆盖侦察 → 入侵 → 横向移动 → 后渗透全流程，自动编排攻击链（疑为 GitHub Trending 榜首的全自动 AI 渗透测试员） | [gadievron/raptor](https://github.com/gadievron/raptor) |
| `Claude-Red` | ![GitHub Repo stars](https://img.shields.io/github/stars/SnailSploit/Claude-Red?style=social) | 2026-08-30 | 37 个即插即用的攻击性安全技能 —— Web 攻击（SQLi/XSS/SSRF/SSTI/XXE）、Shellcode 编写、EDR 规避、漏洞利用开发、红队行动、OSINT、模糊测试等 | [SnailSploit/Claude-Red](https://github.com/SnailSploit/Claude-Red) |
| `Claude-OSINT` | ![GitHub Repo stars](https://img.shields.io/github/stars/elementalsouls/Claude-OSINT?style=social) | 2026-08-30 | OSINT / 侦察技能包 —— 8 个 skill、100+ 侦察能力、80 个 secret-regex 模式、80+ Google dorks、9 个只读凭证验证器、27 个攻击路径模板，约万行结构化 tradecraft | [elementalsouls/Claude-OSINT](https://github.com/elementalsouls/Claude-OSINT) |
| `iothackbot` | ![GitHub Repo stars](https://img.shields.io/github/stars/BrownFineSecurity/iothackbot?style=social) | 2026-06-01 | IoT 渗透测试技能集 + 混合 IoT pentest 工具链（固件分析、硬件接口、无线协议等） | [BrownFineSecurity/iothackbot](https://github.com/BrownFineSecurity/iothackbot) |
| `cti-expert` | ![GitHub Repo stars](https://img.shields.io/github/stars/7onez/cti-expert?style=social) | 2026-08-28 | 网络威胁情报（CTI）& OSINT 分析技能 —— 67+ commands、35 项技术，IOC 提取、威胁画像、情报收集与关联，无需 API key | [7onez/cti-expert](https://github.com/7onez/cti-expert) |
| `communitytools` | ![GitHub Repo stars](https://img.shields.io/github/stars/transilienceai/communitytools?style=social) | 2026-07-29 | 面向 AI 驱动渗透测试的开源 skills / agents / slash commands 集合 | [transilienceai/communitytools](https://github.com/transilienceai/communitytools) |
| `skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/SpecterOps/skills?style=social) | 2026-09-03 | SpecterOps（BloodHound 作者公司）出品的红队 AI skills marketplace，Outflank 与 Fortra 协作共建（[发布公告](https://www.outflank.nl/blog/2026/09/02/red-team-ai-skills/)）—— 26 个插件覆盖 C2（Cobalt Strike/Mythic/Outflank C2）、AD 攻防（ADCS/SCCM/MSSQL/侦察）、Windows/Linux/mac 三平台 tradecraft、payload、社工、逆向、报告生成，集成 BloodHound/Ghostwriter/Binary Ninja MCP，对标 Trail of Bits marketplace | [SpecterOps/skills](https://github.com/SpecterOps/skills) |
| `bountyforge` | ![GitHub Repo stars](https://img.shields.io/github/stars/Gabson0x/bountyforge?style=social) | 2026-08-29 | 全能 bug bounty 技能 —— 8 个专项 agent 并行攻击不同面：Web/API（IDOR/XSS/SSRF/SQLi/GraphQL/CORS 等）+ 智能合约审计（EVM/Move/Solana/TRON），发现去重、CVSS 打分，产出 HackerOne/Bugcrowd/Intigriti/Immunefi 提交级报告 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) |
| `Claude-Code-CyberSecurity-Skill` | ![GitHub Repo stars](https://img.shields.io/github/stars/Masriyan/Claude-Code-CyberSecurity-Skill?style=social) | 2026-09-03 | 19 个 Claude Code 安全技能，覆盖攻击性安全、防御运营、逆向工程、威胁狩猎、CSOC 自动化、红队行动、密码分析等，较为全面的 Cybersecurity 技能集合 | [Masriyan/Claude-Code-CyberSecurity-Skill](https://github.com/Masriyan/Claude-Code-CyberSecurity-Skill) |
| `awesome-skills-security` | ![GitHub Repo stars](https://img.shields.io/github/stars/Eyadkelleh/awesome-skills-security?style=social) | 2026-06-08 | 从 SecLists 打包的安全测试工具包，提供 wordlists、injection payloads、patterns、webshells 等，即插即用，适合 pentest、CTF、bug bounty | [Eyadkelleh/awesome-skills-security](https://github.com/Eyadkelleh/awesome-skills-security) |
| `Black-cat` | ![GitHub Repo stars](https://img.shields.io/github/stars/0rangec3t/Black-cat?style=social) | 2026-08-03 | 假设-证据驱动的红队技能（Hypothesis-Driven Cognitive Architecture）—— 区别于流水线式 pentest skill，采用状态机设计（RECON ⇄ ENUMERATE ⇄ VALIDATE），失败与新发现可回溯重启早期阶段；覆盖信息收集、Web 渗透、内网横向、云安全、EDR 规避、数据库利用、逆向工程等 7 个 technique | [0rangec3t/Black-cat](https://github.com/0rangec3t/Black-cat) |
| `pentest-skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/crazyMarky/pentest-skills?style=social) | 2026-06-04 | 模块化渗透测试技能 —— 自然语言驱动专业级 pentest（信息收集 → 漏洞利用 → 后渗透），支持 Claude Code / Gemini CLI | [crazyMarky/pentest-skills](https://github.com/crazyMarky/pentest-skills) |
| `red-run` | ![GitHub Repo stars](https://img.shields.io/github/stars/blacklanternsecurity/red-run?style=social) | 2026-04-01 | 攻击性安全工具包，结合 Skills + MCP Servers + Agent Teams，实现 recon → initial access → lateral movement → privilege escalation → post-access 完整红队流程路由 | [blacklanternsecurity/red-run](https://github.com/blacklanternsecurity/red-run) |
| `av-evasion-skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/bluechips-zhao/av-evasion-skills?style=social) | 2026-08-10 | Shellcode 免杀技能 v5.2 —— Indirect Syscall、ETW 补丁、Module Stomping、.text Code Cave、IPv4/XOR 混淆、HeapAlloc 缓冲等技术，从静态特征、行为轨迹、EDR 感知三层绕过主流杀软与 EDR（Python 处理脚本 + C Loader 完整生成链） | [bluechips-zhao/av-evasion-skills](https://github.com/bluechips-zhao/av-evasion-skills) |
| `Claude-AD` | ![GitHub Repo stars](https://img.shields.io/github/stars/ADScanPro/Claude-AD?style=social) | 2026-08-24 | Active Directory 内网渗透方法论 —— 阶段顺序、环境约束、技术遥测与合规映射，覆盖 Kerberoasting、ADCS ESC1-17、DCSync、NTLM Relay；驱动 netexec/impacket/certipy/bloodyAD/BloodHound CE 标准工具链（skills + agents + slash commands） | [ADScanPro/Claude-AD](https://github.com/ADScanPro/Claude-AD) |
| `kali-pentest` | ![GitHub Repo stars](https://img.shields.io/github/stars/x-glacier/kali-pentest?style=social) | 2026-06-25 | Kali Linux 渗透测试技能 —— 269 个 CLI 工具 14 类，agent 经 SSH/Docker 接入 Kali 后自主规划攻击路径、跨阶段整合分析并产出结构化报告；15 场景 playbook、授权检查与高危动作人工确认门，支持 Claude Code/OpenClaw/Hermes | [x-glacier/kali-pentest](https://github.com/x-glacier/kali-pentest) |
| `ThreatSwarm` | ![GitHub Repo stars](https://img.shields.io/github/stars/mukul975/Threatswarm?style=social) | 2026-04-29 | 27 个 scope 强制 agent 组成的全 kill-chain 渗透插件 —— recon → exploit → post-ex → DFIR → 报告一条命令跑完，背后由 754 个 MITRE ATT&CK 映射技能驱动（与 [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) 同作者） | [mukul975/Threatswarm](https://github.com/mukul975/Threatswarm) |
| `supabase-pentest-skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/yoanbernabeu/supabase-pentest-skills?style=social) | 2026-01-31 | Supabase 应用安全审计专项 —— 24 个 skill 覆盖 secret key 提取、RLS 策略测试、IDOR 检测、存储桶审计、证据收集与综合报告 | [yoanbernabeu/supabase-pentest-skills](https://github.com/yoanbernabeu/supabase-pentest-skills) |
| `claude-code-pentest` | ![GitHub Repo stars](https://img.shields.io/github/stars/Orizon-eu/claude-code-pentest?style=social) | 2026-03-11 | 6 个 skill 自动化完整 pentest 生命周期 —— 给一个域名，从 recon 到漏洞利用链再到 bug bounty 报告；43 个脚本零 pip 依赖 | [Orizon-eu/claude-code-pentest](https://github.com/Orizon-eu/claude-code-pentest) |
| `src-6k-security-research-skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/jiker666/src-6k-security-research-skills?style=social) | 2026-09-02 | SRC 众测安全研究技能包 —— 黑盒 SRC 挖掘、固定范围测试、品牌/集团资产发现、JS/API 分析、漏洞验证、中文报告与白盒 0day 审计；48 个按需加载专题模块、L0-L4 分层运行时规则、Evidence-First 证据链方法论（Signal → Hypothesis → Controlled Test → Differential Evidence → Impact → Finding），内置 FOFA MCP | [jiker666/src-6k-security-research-skills](https://github.com/jiker666/src-6k-security-research-skills) |

### 逆向工程

| 技能 | Star | 更新时间 | 说明 | 仓库 |
| --- | --- | --- | --- | --- |
| `reverse-skill` | ![GitHub Repo stars](https://img.shields.io/github/stars/zhaoxuya520/reverse-skill?style=social) | 2026-09-03 | 逆向/渗透/安全研究技能路由包 —— AI 自动路由（识别任务类型匹配方法论）+ 按需自举工具链 + 自动进化经验库；覆盖 Android/iOS/二进制/.NET/JS 逆向、恶意代码分析、Pwn、CTF（40+ 子技能）、固件 IoT、N-day、EDR 规避、API 安全、LLM 安全等 18+ 场景；支持 Claude Code / Kiro / Cursor / Cline 等 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) |
| `android-reverse-engineering` | ![GitHub Repo stars](https://img.shields.io/github/stars/SimoneAvogadro/android-reverse-engineering-skill?style=social) | 2026-06-10 | Android APK/XAPK/JAR/AAR 逆向 —— jadx 反编译、Retrofit/OkHttp API 提取、调用流追踪、ProGuard 混淆分析 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) |
| `reverse-engineering` | ![GitHub Repo stars](https://img.shields.io/github/stars/P4nda0s/reverse-skills?style=social) | 2026-05-06 | 二进制逆向工程 —— 配合 IDA-NO-MCP 导出反编译结果，分析函数符号、重建数据结构（rev-symbol / rev-struct） | [P4nda0s/reverse-skills](https://github.com/P4nda0s/reverse-skills) |
| `android-reverse-engineering-codex` | ![GitHub Repo stars](https://img.shields.io/github/stars/CreditTone/android-reverse-engineering-skill?style=social) | 2026-05-07 | 专为 Codex 适配的 Android 逆向分析技能 —— jadx + Fernflower/Vineflower 反编译 APK/XAPK/JAR/AAR，梳理 Manifest/包结构/网络层/调用链，提取接口/URL/鉴权头/token/签名逻辑，并提供 Frida、抓包、JNI/SO 分析前的静态侦察方法（与同名 [SimoneAvogadro](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) 的 Claude Code 版不同，本仓库面向 Codex） | [CreditTone/android-reverse-engineering-skill](https://github.com/CreditTone/android-reverse-engineering-skill) |
| `ai-mobile-reverse-skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/Fausto-404/ai-mobile-reverse-skills?style=social) | 2026-08-14 | 移动安全分析 6 阶段总控 —— APK 静态侦察、流量与代码对齐、SO/JNI 深度分析、加密与漏洞综合分析、验证设计与报告交付，支持 JADX/Burp/Yakit/IDA/Ghidra MCP | [Fausto-404/ai-mobile-reverse-skills](https://github.com/Fausto-404/ai-mobile-reverse-skills) |
| `android-reverse-engineering-claude-skill` | ![GitHub Repo stars](https://img.shields.io/github/stars/incogbyte/android-reverse-engineering-claude-skill?style=social) | 2026-06-20 | Android 逆向自动化技能 —— APK/XAPK/AAB/DEX/JAR/AAR 反编译（jadx + Fernflower）、Retrofit/OkHttp HTTP 端点提取 | [incogbyte/android-reverse-engineering-claude-skill](https://github.com/incogbyte/android-reverse-engineering-claude-skill) |

### 代码审计

| 技能 | Star | 更新时间 | 说明 | 仓库 |
| --- | --- | --- | --- | --- |
| `VibeSec-Skill` | ![GitHub Repo stars](https://img.shields.io/github/stars/BehiSecc/VibeSec-Skill?style=social) | 2026-02-17 | 安全优先代码审查 —— 以漏洞猎手视角审视代码，捕获 Web 应用常见漏洞（OWASP Top 10），防御性安全辅助 | [BehiSecc/VibeSec-Skill](https://github.com/BehiSecc/VibeSec-Skill) |
| `audit-skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/RuoJi6/audit-skills?style=social) | 2026-06-16 | Java Web 源码安全审计 —— 路由提取、SQL 注入/XXE/文件上传/鉴权绕过多维度自动化审计；轻量化设计，只负责安全边界（原 `java-audit-skills`，已改名） | [RuoJi6/audit-skills](https://github.com/RuoJi6/audit-skills) |
| `code-audit` | ![GitHub Repo stars](https://img.shields.io/github/stars/3stoneBrother/code-audit?style=social) | 2026-02-13 | 通用代码审计 —— 支持 55+ 漏洞类型，双轨审计模型（自动化 + 专家模式），覆盖 Java/Python/Go/PHP/JS/C 等多语言 | [3stoneBrother/code-audit](https://github.com/3stoneBrother/code-audit) |
| `PHP_AUDIT_SKILLS` | ![GitHub Repo stars](https://img.shields.io/github/stars/yunmengya/PHP_AUDIT_SKILLS?style=social) | 2026-05-08 | PHP 代码审计 —— 基于 Agent Teams 多智能体协作，静态分析 + 动态追踪 + AI 辅助三重审计，覆盖 21 种漏洞类型 | [yunmengya/PHP_AUDIT_SKILLS](https://github.com/yunmengya/PHP_AUDIT_SKILLS) |

### 漏洞知识库

| 技能 | Star | 更新时间 | 说明 | 仓库 |
| --- | --- | --- | --- | --- |
| `wooyun-legacy` | ![GitHub Repo stars](https://img.shields.io/github/stars/tanweai/wooyun-legacy?style=social) | 2026-07-14 | WooYun 漏洞知识库 —— 88,636 个真实漏洞案例（SQL 注入 27%、命令执行 19%、XSS 11% 等 15 种类型），86MB 精炼安全方法论 | [tanweai/wooyun-legacy](https://github.com/tanweai/wooyun-legacy) |
| `secknowledge-skill` | ![GitHub Repo stars](https://img.shields.io/github/stars/Pa55w0rd/secknowledge-skill?style=social) | 2026-06-17 | Web 与 AI 安全测试知识技能 —— 克隆到 skills 目录后自动加载，提供测试方法论与安全知识库 | [Pa55w0rd/secknowledge-skill](https://github.com/Pa55w0rd/secknowledge-skill) |

### 综合安全仓库

| 技能 | Star | 更新时间 | 说明 | 仓库 |
| --- | --- | --- | --- | --- |
| `Anthropic-Cybersecurity-Skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/mukul975/Anthropic-Cybersecurity-Skills?style=social) | 2026-08-31 | 817 个结构化网络安全技能，映射 MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF、MITRE F3 等 6 大框架，覆盖 29 个安全域、进攻 / 防御 / 合规全谱系，支持 Claude Code / Copilot / Codex / Cursor / Gemini CLI 等 20+ 平台，目前规模最大的 AI 安全技能库 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) |
| `claude-skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/alirezarezvani/claude-skills?style=social) | 2026-08-30 | 380+ 技能大型集合（30+ Agents、70+ 自定义命令），包含多个安全相关子技能：senior-security（威胁建模/渗透测试/OWASP）、ai-security（Prompt 注入检测/模型安全）、cloud-security（CSPM 云安全）、security-pen-testing 等，推荐作为技能库底座 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) |
| `skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/trailofbits/skills?style=social) | 2026-09-02 | Trail of Bits 出品，17+ 安全研究技能 —— 漏洞检测、差分代码审查、审计上下文构建、修复验证，专注安全研究、漏洞检测与审计工作流，质量较高 | [trailofbits/skills](https://github.com/trailofbits/skills) |
| `SecSkills` | ![GitHub Repo stars](https://img.shields.io/github/stars/DaoYiSec/SecSkills?style=social) | 2026-07-06 | 刀义安全出品，53 个安全技能索引，覆盖代码审计、渗透测试、JS 逆向、CTF、红蓝对抗、移动安全、应急响应等 16 个分类 | [DaoYiSec/SecSkills](https://github.com/DaoYiSec/SecSkills) |
| `openclaw-sec-skills` | ![GitHub Repo stars](https://img.shields.io/github/stars/Batman0506/openclaw-sec-skills?style=social) | 2026-06-25 | OpenClaw 社区安全技能大全，150+ 技能索引，涵盖代码审计、渗透测试、逆向工程、CTF、威胁建模、移动安全、应急响应、安全工具 8 大领域 | [Batman0506/openclaw-sec-skills](https://github.com/Batman0506/openclaw-sec-skills) |

## 许可证

MIT 许可证 —— 详见 [LICENSE](LICENSE)。
