## 先校准一下比较对象

截至 **2026 年 6 月 26 日**，三者并不完全处于同一层级：

| 厂商        | 当前适合拿来比较的组合                        | 说明                                                                                                                        |
| --------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Anthropic | **Claude Opus 4.8 + Claude Code**  | Claude Fable 5 技术上更新，但自 6 月 12 日起仍暂停访问，因此实际开发应以 Opus 4.8 为准。([Anthropic][1])                                              |
| OpenAI    | **Codex + GPT-5.5**                | Codex 是编码代理和开发环境，不是单一模型；当前官方推荐模型是 GPT-5.5。([OpenAI开发者][2])                                                                |
| Google    | **Gemini 3.5 Flash + Antigravity** | Gemini 3.5 Flash 是最新已发布模型；Gemini 3.5 Pro 仍标记为“coming soon”。面向个人开发者的 Gemini CLI 已转向 Antigravity CLI。([Google DeepMind][3]) |

## 核心结论

可以把它们理解成三种不同类型的“团队成员”：

* **Claude：总设计师、架构师、高级代码审查员**
* **Codex：主程、集成工程师、测试与交付负责人**
* **Gemini：多模态设计师、高吞吐副手、Google 技术栈专家**

开发游戏时，比较理想的搭配不是让三个模型同时写同一批代码，而是：

> **Claude 定规范和审查，Codex 负责实现与验证，Gemini 负责视觉、多媒体、高频批量任务。**

---

## 项目完成能力对比

以下是实践取向的判断，不是单一跑分排名。

| 维度                            | Claude Opus 4.8                  | Codex + GPT-5.5                               | Gemini 3.5 Flash                                        |
| ----------------------------- | -------------------------------- | --------------------------------------------- | ------------------------------------------------------- |
| 需求理解与系统设计                     | **最强项之一**，擅长处理模糊需求、系统边界、不变量和长期演进 | 强，更偏向把需求快速变成执行计划                              | 强，适合快速探索多个方案，但深层架构建议最好再审查                               |
| 复杂代码库理解                       | **很强**，适合跨模块分析、大型重构和根因排查         | **很强**，尤其擅长找到修改点后直接完成代码、测试和验证                 | 强，1M 上下文适合大量文件和资料，但 Flash 更偏速度与规模                       |
| 实际写代码                         | 强，通常比较谨慎、结构化                     | **三者中最适合作为主执行者**                              | 强，尤其适合快速迭代、前端、Web 和大量相似任务                               |
| 调试、测试、跑命令                     | 强，擅长推理复杂故障                       | **最完整**，实现、重构、调试、测试、验证是一体化工作流                 | 强，Antigravity 可运行代码、管理文件、使用沙箱和子代理                       |
| 长时间自主完成任务                     | 很强，尤其适合复杂迁移和高自治任务                | **很强且工程闭环较完整**，适合从 Issue 做到可合并改动              | **高吞吐优势明显**，适合多个子代理并行推进                                 |
| GUI、浏览器和实际操作                  | Claude Code 可以使用工具，但不是其最突出差异点    | **突出优势**，可操作 macOS/Windows GUI、浏览器、模拟器并复现界面问题 | 强，支持 computer use 预览，Antigravity 也强调浏览器和沙箱操作            |
| 图片、视频、音频理解                    | 原生支持文本和图片输入；视频通常需要拆帧             | 原生模型以文本、图片输入为主，但 Codex 可操作屏幕和浏览器              | **明显最强**，直接接受文本、图片、视频、音频和 PDF                           |
| 前端、视觉和交互探索                    | 擅长把设计要求写得细致且保持风格一致               | 擅长把设计直接做成可运行界面并在浏览器验证                         | **适合快速生成多个 UX/UI 方向，并分析录屏和截图**                          |
| Android、Firebase、Google Cloud | 可开发，但没有平台原生优势                    | 可开发并维护完整工程                                    | **明显优势**，与 Android、Firebase、Cloud、Maps 和 AI Studio 集成最深 |
| 成本与高频使用                       | 能力强，但成本和延迟较高                     | 能力强，GPT-5.5 成本较高                              | **最适合大批量调用和子代理任务**                                      |

Claude Code 官方定位包括读取整个代码库、编辑文件、运行命令、代码审查、调试及长周期代理式编码；Codex 官方尤其强调实现、重构、测试、验证、计算机操作和并行工作树；Gemini 3.5 Flash 则专门针对子代理、多步骤工作流、长周期任务和快速编码循环优化。([Anthropic][4])

### 跑分透露出的实际差异

Google 公布的同一组测试里，没有一个模型全面第一：

* Terminal-Bench 2.1：GPT-5.5 为 78.2%，Gemini 3.5 Flash 为 76.2%；
* SWE-Bench Pro：Claude Opus 4.7 为 64.3%，GPT-5.5 为 58.6%，Gemini 3.5 Flash 为 55.1%；
* MCP Atlas：Gemini 3.5 Flash 为 83.6%，Claude Opus 4.7 为 79.1%，GPT-5.5 为 75.3%。

这大致对应三家的特点：Codex 偏终端工程执行，Claude 偏复杂代码修复和严谨性，Gemini 偏多工具、多代理工作流。不过该表里的 Claude 还是 4.7，并非最新的 4.8，且厂商跑分会受代理框架和测试设置影响，只适合看趋势。([Google DeepMind][3])

---

## 各自最擅长什么

### Claude Opus 4.8：复杂系统、架构和审查

最适合交给 Claude 的任务：

* 游戏系统架构：ECS、技能系统、状态机、事件系统、存档系统；
* 多人同步、回滚、确定性模拟等需要严密推理的模块；
* 在动手前分析系统边界、数据契约和潜在失败模式；
* 大规模重构方案和代码审查；
* 疑难 Bug 根因分析；
* 剧情圣经、任务线、角色关系和世界观一致性；
* 把零散想法整理成完整 GDD、技术设计文档和验收标准。

Opus 4.8 具有 1M 上下文、128K 最大输出，Anthropic 将其定位为复杂推理、长周期代理式编码和高自治工作的模型，并特别强调更好的长上下文处理、工具触发和错误自检。([Claude Platform Docs][5])

主要短板是成本和速度。其 API 标准价格为每百万输入/输出 token **5/25 美元**，适合用在高价值设计、审查和疑难任务上，不建议拿来批量生成几百个相似配置文件。([Claude Platform Docs][6])

### Codex + GPT-5.5：真正把项目做出来

最适合交给 Codex 的任务：

* 初始化项目、安装依赖、搭建目录结构；
* 实现完整功能，而不是只给代码片段；
* 跨文件修改、重构、补测试；
* 运行编译、单元测试、集成测试和静态检查；
* 修复报错后再次运行验证；
* Git 分支、worktree、提交、PR 和代码审查；
* 浏览器中运行游戏、测试操作和 UI；
* 操作桌面软件、模拟器或编辑器，复现 GUI 问题；
* CI/CD、打包、版本号和发布脚本。

OpenAI 官方把 GPT-5.5 推荐为 Codex 中大多数任务的首选，特别包括实现、重构、调试、测试和验证；Codex App 本身还提供并行线程、worktree、Git、浏览器和计算机操作。OpenAI 甚至有专门的浏览器游戏工作流，让 Codex 从游戏 Brief 开始，生成游戏、调用图像工具并在实时浏览器中测试。([OpenAI开发者][2])

GPT-5.5 在 API 中有约 1.05M 上下文和 128K 输出，但在 Codex 产品内为 **400K 上下文**。API 标准价格为每百万输入/输出 token **5/30 美元**。([OpenAI开发者][7])

它的风险来自执行力本身：权限和任务范围写得不清楚时，可能修改比预想更多的文件。因此应使用独立分支、worktree、限制目录范围，并要求每次提交测试证据。

### Gemini 3.5 Flash：多模态、速度、规模和 Google 生态

最适合交给 Gemini 的任务：

* 分析游戏截图、操作录屏、UI 原型和音频；
* 根据一段玩法视频找出节奏、可读性和反馈问题；
* 快速产生多个交互方案或 Web UI 方案；
* 批量生成配置、数据校验器、内容导入工具；
* 多个子代理并行探索不同实现；
* Android、Kotlin、Firebase、Cloud Run、Google Play 相关工作；
* 大量日志、文档、图片和 PDF 的综合分析；
* 高并发、成本敏感的日常开发任务。

Gemini 3.5 Flash 支持约 1.048M 输入和 65K 输出，可直接输入文本、图片、视频、音频和 PDF，并支持代码执行、文件搜索、函数调用、搜索与 Maps grounding，以及 computer use 预览。Antigravity 则支持多代理、异步工作流、沙箱、Hooks 和 Skills。([Google AI for Developers][8])

它的标准 API 价格为每百万输入/输出 token **1.5/9 美元**，明显低于 Opus 4.8 和 GPT-5.5，因此特别适合作为批量副手。([Google AI for Developers][9])

主要限制是：当前发布的是 **Flash 而不是 3.5 Pro**。虽然编码能力很强，但遇到极难的架构、并发、网络同步或跨系统重构，我仍会让 Claude 或 GPT-5.5 做最终审查。

---

## 开发游戏时的最佳搭配

### 1. 立项和设计阶段：Claude 主导，Gemini 辅助

让 Claude 负责：

* 游戏核心循环；
* GDD；
* 系统拆分；
* 数据模型；
* 技术选型；
* 风险清单；
* 可测试的验收条件；
* MVP 和垂直切片范围。

让 Gemini 负责：

* 分析参考游戏的视频和截图；
* 比较不同 UI、镜头和操作方式；
* 生成多个视觉与交互方向；
* 根据目标平台分析屏幕尺寸、输入方式和可读性。

这个阶段不要急着让三个模型同时写代码。先把 `GDD.md` 和 `ARCHITECTURE.md` 定下来。

### 2. 垂直切片阶段：Codex 主导实现

让 Codex 独立负责一个最小可玩的闭环，例如：

> 启动游戏 → 进入关卡 → 移动/战斗 → 获得奖励 → 失败或通关 → 重新开始。

Codex 的任务必须包含：

* 实现代码；
* 启动项目；
* 跑测试；
* 实际运行游戏；
* 验证输入和 UI；
* 报告修改文件；
* 提供通过和失败的测试证据。

浏览器游戏可以直接让 Codex 在浏览器里玩；Unity、Godot 或 Unreal 项目，则让它负责代码、构建、日志和可自动化的编辑器操作。

### 3. 核心系统阶段：Claude 设计，Codex 实现

推荐采用固定循环：

1. **Claude 写规格**：接口、状态转换、不变量、失败模式、验收测试；
2. **Codex 实现**：代码、迁移、测试和运行验证；
3. **Claude 审查**：检查架构偏离、隐藏耦合和边界条件；
4. **Codex 修复并重新跑测试**。

尤其适合：

* 存档与版本迁移；
* 技能和 Buff 系统；
* AI 行为树；
* 网络同步；
* 任务系统；
* 物品与经济系统；
* 战斗公式；
* 程序化生成。

### 4. UI、美术和玩法反馈：Gemini 分析，Codex 落地

每次提交一个可玩版本后，可以给 Gemini：

* 30～90 秒游戏录屏；
* 不同分辨率的截图；
* 输入延迟日志；
* 帧率和性能日志；
* 玩家测试记录。

让它输出：

* 严重程度；
* 复现步骤；
* 视觉层级问题；
* 操作反馈问题；
* 节奏和信息过载问题；
* 针对手机、PC、手柄的差异；
* 可直接创建为 Issue 的修改建议。

然后由 Codex 根据 Issue 修改并运行验证。

### 5. QA 和发布阶段：Codex 执行，Gemini 批量检查，Claude处理疑难问题

Codex：

* 单元测试、集成测试和冒烟测试；
* 构建多个平台；
* 检查资源路径和缺失引用；
* CI/CD；
* 打包和版本管理；
* 自动化回归。

Gemini：

* 批量分析录屏、截图、日志和崩溃报告；
* 本地化长度、UI 溢出和素材一致性检查；
* Android/Firebase/Google Play 相关集成。

Claude：

* 难以复现的状态 Bug；
* 性能架构问题；
* 网络竞态；
* 存档损坏；
* 发布前代码和设计审查。

---

## 不同游戏类型的推荐比例

### Web、HTML5、小游戏

**Codex 60% / Gemini 25% / Claude 15%**

Codex 负责主工程和浏览器测试，Gemini负责 UI/视觉和快速变体，Claude审查核心设计。

### Unity、Godot、Unreal 独立游戏

**Codex 50% / Claude 30% / Gemini 20%**

Codex 是主程，Claude负责系统架构和疑难问题，Gemini负责录屏、截图、素材和 UX 分析。

### Android 或 Firebase 后端游戏

**Gemini 40% / Codex 40% / Claude 20%**

Gemini负责 Android、Firebase、Cloud 和平台集成；Codex负责游戏代码、测试和构建；Claude负责架构审查。Google AI Studio 已提供原生 Kotlin、Firebase 和 Cloud Run 相关开发集成。([谷歌开发者博客][10])

### 剧情 RPG、视觉小说、任务驱动游戏

**Claude 40% / Codex 40% / Gemini 20%**

Claude维护世界观、人物弧光、任务依赖和文本风格，Codex实现对话与任务系统，Gemini分析 UI、配音和演出素材。

---

## 必须建立的项目协作规则

最重要的是实行 **单一写入者原则**：

> 同一个功能、同一个分支、同一组文件，只允许一个模型负责写；其他模型只做设计或审查。

建议仓库至少包含：

```text
/docs/GDD.md
/docs/ARCHITECTURE.md
/docs/DECISIONS.md
/docs/ACCEPTANCE_TESTS.md
/docs/CONTENT_SCHEMA.md

AGENTS.md
CLAUDE.md
/.agents/skills/game-qa/SKILL.md
```

其中：

* `AGENTS.md` 给 Codex 保存构建命令、测试要求、代码规范和允许修改的目录；
* `CLAUDE.md` 给 Claude 保存架构原则、设计约束和审查标准；
* `.agents/skills/` 给 Antigravity 保存视觉 QA、内容检查等可复用流程。

三套工具都支持把项目约束放入仓库内的持久化指令或 Skills，而不是每次重新解释。([OpenAI开发者][11])

## 直接可复制的任务模板

**给 Claude：**

```text
只做设计和审查，暂时不要修改代码。

读取：
- docs/GDD.md
- docs/ARCHITECTURE.md
- docs/DECISIONS.md

针对“战斗技能系统”输出：
1. 系统边界
2. 数据契约
3. 必须保持的不变量
4. 状态转换
5. 失败模式和边界情况
6. 可自动化的验收测试
7. 建议 Codex 修改的文件范围
```

**给 Codex：**

```text
按照 docs/ACCEPTANCE_TESTS.md 实现 Issue #42。

要求：
- 在独立 worktree/分支中工作
- 只修改 Combat、Tests 和必要的配置目录
- 先检查现有实现和测试，不要重复造轮子
- 完成后运行单元测试、集成测试和构建
- 报告修改文件、执行命令、测试结果和未解决风险
- 测试未通过时不要宣称任务完成
```

**给 Gemini：**

```text
分析 gameplay.mp4、screenshots/ 和 profiler-logs/。

重点检查：
- 玩家是否清楚当前目标
- 输入反馈和攻击命中反馈
- UI 视觉层级
- 战斗节奏
- 文本与按钮在不同分辨率下的可读性
- 帧率下降对应的画面事件

输出按 P0/P1/P2/P3 排序的 Issue 列表，
每项包含复现时间点、问题证据、预期行为和验收条件。
```

## 关于游戏素材的一个重要区别

“能看懂图片和视频”不等于“当前主模型能直接生成最终素材”：

* Claude 当前是文本和图片输入、文本输出；
* GPT-5.5 本身以文本输出为主，但 Codex 可以调用图像生成工具并把素材放入工程；
* Gemini 3.5 Flash 能理解图片、视频和音频，但其模型页明确标记不直接支持图像生成，需要搭配 Gemini 3.1 Flash Image 或 Gemini 3 Pro Image。([Claude Platform Docs][12])

因此，对大多数独立游戏团队，最实用的组合是：

> **Codex 作为每天打开的主开发环境；Claude 用在设计评审、复杂系统和疑难 Bug；Gemini 用在录屏分析、UI/视觉、高频批处理以及 Android/Google 生态。**

三家一起使用的价值不在于“让三个模型投票”，而在于把它们放进一条有明确责任人的流水线：**Claude 定义正确，Codex把它做出来，Gemini检查玩家实际看到和感受到的东西。**

[1]: https://www.anthropic.com/news/fable-mythos-access?utm_source=chatgpt.com "Statement on the US government directive to suspend ..."
[2]: https://developers.openai.com/codex/models?utm_source=chatgpt.com "Codex Models"
[3]: https://deepmind.google/models/gemini/ "Gemini 3.5 — Google DeepMind"
[4]: https://www.anthropic.com/news/claude-opus-4-8?utm_source=chatgpt.com "Introducing Claude Opus 4.8"
[5]: https://docs.anthropic.com/en/docs/about-claude/models/whats-new-claude-4-8?utm_source=chatgpt.com "What's new in Claude Opus 4.8"
[6]: https://docs.anthropic.com/en/docs/about-claude/pricing "Pricing - Claude Platform Docs"
[7]: https://developers.openai.com/api/docs/models/gpt-5.5 "GPT-5.5 Model | OpenAI API"
[8]: https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash "Gemini 3.5 Flash  |  Gemini API  |  Google AI for Developers"
[9]: https://ai.google.dev/gemini-api/docs/pricing "Gemini Developer API pricing  |  Gemini API  |  Google AI for Developers"
[10]: https://developers.googleblog.com/all-the-news-from-the-google-io-2026-developer-keynote/ "
            
            All the news from the Google I/O 2026 Developer keynote
            
            
            \- Google Developers Blog
            
        "
[11]: https://developers.openai.com/codex/guides/agents-md?utm_source=chatgpt.com "Custom instructions with AGENTS.md – Codex"
[12]: https://docs.anthropic.com/en/docs/about-claude/models/overview "Models overview - Claude Platform Docs"
