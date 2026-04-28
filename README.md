# Skills4RedTeam

面向红队操作人员的攻击性安全技能合集，基于 [Claude-Red](https://github.com/SnailSploit/Claude-Red)。

## 简介

本仓库收录了一套面向 Claude 技能系统的攻击性安全技能。每个技能是一个结构化的 `SKILL.md` 文件，为 Claude 注入针对特定攻击面的专业方法论 —— 从 SQL 注入到 Shellcode 编写，从 EDR 规避到漏洞利用开发。

## 上游项目

本项目基于 **[Claude-Red](https://github.com/SnailSploit/Claude-Red)**，由 [SnailSploit (Kai Aizen)](https://github.com/SnailSploit) 开发 —— 包含 37 个即插即用的攻击性安全技能，让 Claude 成为具备上下文感知能力的红队操作员。

原始检查清单由 Sahar Shlichov 编写。

## 技能索引

### Web 应用安全

| 技能 | 说明 |
| --- | --- |
| `offensive-sqli` | SQL 注入 —— 联合查询、盲注、带外交注、绕过链 |
| `offensive-xss` | 跨站脚本 —— 存储型、反射型、DOM 型、变异型 |
| `offensive-ssrf` | 服务端请求伪造 —— 云元数据、过滤器绕过 |
| `offensive-ssti` | 服务端模板注入 —— 引擎识别、RCE 路径 |
| `offensive-xxe` | XML 外部实体注入 —— 带外泄露、盲注利用 |
| `offensive-idor` | 不安全直接对象引用 —— 枚举、业务逻辑 |
| `offensive-file-upload` | 文件上传漏洞 —— 扩展名绕过、多语言文件、WebShell |
| `offensive-rce` | 远程代码执行 —— 链式利用、命令注入、反序列化 |
| `offensive-deserialization` | 不安全反序列化 —— Java、PHP、.NET 利用链 |
| `offensive-race-condition` | 竞态条件 —— TOCTOU、限制绕过、并发请求攻击 |
| `offensive-request-smuggling` | HTTP 请求走私 —— CL.TE、TE.CL、管道失步 |
| `offensive-open-redirect` | 开放重定向 —— OAuth 滥用、钓鱼链、SSRF 跳板 |
| `offensive-parameter-pollution` | HTTP 参数污染 —— WAF 绕过、逻辑混淆 |
| `offensive-graphql` | GraphQL 漏洞 —— 内省、批处理、别名 IDOR |
| `offensive-waf-bypass` | WAF 绕过技术 —— 编码、分块、大小写变异 |

### 认证与身份

| 技能 | 说明 |
| --- | --- |
| `offensive-jwt` | JWT 安全 —— alg:none、密钥混淆、密钥爆破 |
| `offensive-oauth` | OAuth 安全测试 —— 开放重定向滥用、令牌泄露、PKCE 绕过 |

### 基础设施与二进制

| 技能 | 说明 |
| --- | --- |
| `offensive-shellcode` | Shellcode —— 编写、编码、注入技术 |
| `offensive-edr-evasion` | EDR 规避 —— 脱钩、间接系统调用、PPID 伪造 |
| `offensive-exploit-development` | 漏洞利用开发 —— 栈/堆、ROP 链、缓解措施 |
| `offensive-exploit-dev-course` | 漏洞利用开发（课程）—— 结构化课程格式 |
| `offensive-basic-exploitation` | 基础漏洞利用 —— Linux、缓解措施关闭、入门到中级 |
| `offensive-crash-analysis` | 崩溃分析与可利用性评估 —— 分类、根因分析 |
| `offensive-mitigations` | 现代内核漏洞缓解措施 —— ASLR、CFG、CET、PAC |
| `offensive-windows-mitigations` | Windows 缓解措施 —— ACG、任意代码守卫、Exploit Guard |
| `offensive-windows-boundaries` | 突破 Windows 安全边界 —— 沙箱逃逸、提权 |
| `offensive-keylogger-arch` | 键盘记录器架构 —— 新型研究、输入捕获技术 |
| `offensive-patch-diffing` | 补丁比对 —— 二进制差异、隐蔽 CVE 发现、变体狩猎 |
| `offensive-initial-access` | 现代初始访问 —— 钓鱼、路过式攻击、供应链 |
| `offensive-advanced-redteam` | 高级红队行动 —— 完整攻击链、C2、操作安全 |

### 侦察与 OSINT

| 技能 | 说明 |
| --- | --- |
| `offensive-osint` | OSINT 工具 —— recon-ng、theHarvester、Maltego、自动化流水线 |
| `offensive-osint-methodology` | OSINT 方法论 —— 结构化情报收集框架 |

### 模糊测试与漏洞研究

| 技能 | 说明 |
| --- | --- |
| `offensive-fuzzing` | 模糊测试 —— libFuzzer、AFL++、覆盖率引导、变异策略 |
| `offensive-fuzzing-course` | 模糊测试（课程）—— 结构化课程、通过 Fuzzing 发现漏洞 |
| `offensive-bug-identification` | 缺陷识别 —— 代码审计模式、静态分析触发点 |
| `offensive-vuln-classes` | 漏洞分类 —— 真实案例、根因分类体系 |

### AI 安全

| 技能 | 说明 |
| --- | --- |
| `offensive-ai-security` | AI 渗透测试 —— 提示注入、越狱、RAG 投毒、LLM 滥用 |

### 实用工具

| 技能 | 说明 |
| --- | --- |
| `offensive-fast-checking` | 快速测试检查清单 —— 快速分类、速胜点识别 |

## 使用方法

### Claude Code

```bash
cat Skills/offensive-sqli/SKILL.md | claude --system-file -
```

### Claude 技能系统

将技能文件夹放置到配置的技能路径下（如 `/mnt/skills/user/`），Claude 会根据触发关键词自动加载。

### 手动使用（Claude.ai）

将 `SKILL.md` 的内容粘贴到项目的系统提示中，或作为对话的前置内容。

## 许可证

MIT 许可证 —— 详见 [LICENSE](LICENSE)。
