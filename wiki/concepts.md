# 概念库

这里记录用户关注的概念、方法论和术语解释。

## 驾驭工程

“驾驭工程”是把 AI 当成一个可协作、可调度、可验收的执行系统来使用的一整套方法。它不只关注如何写提示词，还关注任务拆解、上下文组织、约束设置、工具调用、多 agent 分工、结果验证、中断恢复、失败重试，以及如何把 AI 接入真实工作流。

来源：`raw/conversations/2026-06-22-driving-engineering-vs-prompt-engineering.md`

### 相关热门工程谱系

截至 2026-06-24，AI/LLM 领域与“驾驭工程”相邻的热门工程方向包括：

- 上下文工程（Context Engineering）：管理模型可见上下文，包括长期记忆、RAG、状态文件、知识库、工具结果和历史任务压缩。
- 智能体工程（Agent Engineering）：让 agent 能规划、调用工具、执行任务、复查结果，并可靠部署到真实工作流。
- 循环工程（Loop Engineering）：通过目标、检查、修复、继续的循环，让 AI 持续推进任务，减少人工逐条提示。
- Harness Engineering：为 agent 配置代码库、日志、指标、测试、权限、工作区等执行环境，使复杂任务可执行、可观察、可验收。
- 评测工程（Eval Engineering）：用测试集、门禁、评分标准、回归检查衡量 AI 行为，而不是只凭主观感觉判断输出质量。
- RAG / 知识库工程：负责检索、分块、引用、溯源、权限和更新流程，常作为上下文工程的一部分。
- 记忆工程（Memory Engineering）：维护长期记忆、用户偏好、项目状态和断点恢复能力。
- 工具工程 / MCP 工程：为 agent 建立可调用工具、插件和连接器，使其能操作文件、浏览器、数据库、云盘、邮件和脚本。
- 可靠性与安全工程（Reliability / Guardrails Engineering）：处理权限控制、失败重试、审计日志、越权防护、敏感信息和可观测性。
- 多 agent 协同工程（Multi-Agent Engineering）：把任务拆给多个 agent 分工执行和交叉审查。

对用户当前“驾驭工程流”最相关的方向是：驾驭工程 / Loop Engineering、上下文工程、评测工程、多 agent 协同工程、记忆工程。

来源：`raw/conversations/2026-06-24-current-hot-ai-engineering-fields.md`

## 提示词工程

“提示词工程”主要研究如何写 prompt，让模型给出更好的回答。它是驾驭工程的一部分，但不是全部。

来源：`raw/conversations/2026-06-22-driving-engineering-vs-prompt-engineering.md`

## 两者区别

提示词工程更像是“会问 AI”，驾驭工程更像是“会用 AI 干活”。

对比：

| 维度 | 提示词工程 | 驾驭工程 |
|---|---|---|
| 核心对象 | 一次模型回答 | 一个完整任务系统 |
| 关注点 | prompt 写法 | 任务拆解、工具调用、流程控制、验收 |
| 典型产物 | 提示词模板 | 自动化流程、脚本、agent 协作、校验机制 |
| 适用场景 | 问答、写作、总结、生成 | 编程、批处理、数据处理、长任务、复杂项目 |
| 成败标准 | 回答质量 | 任务是否真的完成、可复现、可验收 |

来源：`raw/conversations/2026-06-22-driving-engineering-vs-prompt-engineering.md`

## 用户当前实践

用户近期使用交接文档定义任务，用约束控制范围，用脚本和工具落地，用校验报告验收结果。这种使用方式已经超出单纯提示词工程，更接近驾驭工程。

来源：`raw/conversations/2026-06-22-driving-engineering-vs-prompt-engineering.md`

## 先提问再执行

“先提问再执行”是提示词工程和驾驭工程之间的一种实用桥梁。它把一次性 prompt 改造成交互式需求澄清流程，让 AI 在执行前先帮助用户发现盲点、明确边界和形成验收标准。

来源：`raw/sources/2026-06-26-jikoujiang-ask-before-execute-prompt-video-analysis.md`

## 单一写入者原则

单一写入者原则用于多模型或多 agent 协作：同一功能、同一分支、同一组文件只安排一个执行者写入，其他 agent 负责设计、审查或验证，避免并行修改造成冲突和责任不清。

来源：`raw/sources/2026-06-26-ai-coding-models-game-development-comparison.md`
