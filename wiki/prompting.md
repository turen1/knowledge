# 提示词方法论

这里记录用户长期可复用的提示词、AI 协作协议和需求澄清方法。

## 先提问，再执行

“先提问，再执行”（Ask-Before-Execute）是一种把 AI 从直接执行者切换为引导式导师的工作流。适合复杂需求、产品设计、UI/UX、系统架构、商业分析和游戏功能开发。

核心规则：

- AI 在动手前先通过提问澄清目标、边界、约束和验收标准。
- 每次只问一个问题，降低用户回答负担。
- 从整体方向逐步深入细节。
- 如果用户回答模糊，继续追问到可执行为止。
- 设置问题上限，例如 15 个以内，避免无限追问。
- 执行前复述完整理解并请求确认。

可复用提示词：

```text
在动手之前请先扮演导师，通过提问帮我理清思路。每次只问一个问题，从整体方向开始，逐步深入细节。如果我回答模糊，请追问到清晰为止。控制在 15 个问题以内。确认我的完整想法后才开始执行。
```

来源：`raw/sources/2026-06-26-jikoujiang-ask-before-execute-prompt-video-analysis.md`

## Best Minds

Best Minds 的核心做法是让 AI 引入特定领域顶尖专家的视角，提高问题定义、方案判断和输出标准。适合 UI/UX、架构设计、图形渲染、产品判断等需要专业品控的任务。

来源：`raw/sources/2026-06-26-jikoujiang-ask-before-execute-prompt-video-analysis.md`

## GStack / Office Hours

GStack / Office Hours 适合在编码前检验项目或功能是否值得做，重点追问用户是谁、解决什么痛点、为什么现在、壁垒是什么、如何防守。它可以减少“想当然地实现功能”造成的返工。

来源：`raw/sources/2026-06-26-jikoujiang-ask-before-execute-prompt-video-analysis.md`
