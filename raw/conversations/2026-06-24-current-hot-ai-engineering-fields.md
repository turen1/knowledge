# 当前热门 AI 工程方向

日期：2026-06-24

## 对话背景

用户询问：“当前热门的工程有哪些？”

上下文中，“工程”被理解为 AI/LLM 领域围绕模型落地的工程范式，而不是土木、制造等传统工程。回答将这些方向关联到用户此前关注的“驾驭工程”。

## 回答要点

当前热门的 AI/LLM 工程方向包括：

1. 上下文工程（Context Engineering）：从“写好提示词”升级为“管理模型能看到什么”，包括长期记忆、RAG、状态文件、知识库、工具结果、历史任务压缩。
2. 智能体工程（Agent Engineering）：让 agent 能规划、调用工具、执行任务、复查结果，重点转向可靠部署和规模化运行。
3. 循环工程（Loop Engineering）：给 AI 一个目标和执行循环，让它持续执行、验证、修复、继续，而不是依赖人不断手写 prompt。
4. 驾驭工程 / Harness Engineering：给 Codex 或 agent 配好代码库、日志、指标、测试、权限、工作区，让 agent 真能完成复杂任务。
5. 评测工程（Eval Engineering）：给 AI 行为建立测试集、门禁、评分标准、回归检查。
6. RAG 工程 / 知识库工程：做检索、分块、引用、溯源、权限、更新流程，通常被纳入上下文工程。
7. 记忆工程（Memory Engineering）：管理长期记忆、用户偏好、项目状态、任务恢复。
8. 工具工程 / MCP 工程：给 agent 写好可调用工具、插件、连接器，使其能操作文件、浏览器、数据库、云盘、邮件、脚本。
9. 可靠性与安全工程（Reliability / Guardrails Engineering）：包括权限控制、失败重试、审计日志、越权防护、敏感信息处理、可观测性。
10. 多 agent 协同工程（Multi-Agent Engineering）：把任务拆给多个 agent，例如一个写、一个审、一个查一致性、一个跑测试。

## 与用户项目的关联

对用户当前项目最相关的排序：

1. 驾驭工程 / Loop Engineering
2. 上下文工程
3. 评测工程
4. 多 agent 协同工程
5. 记忆工程

用户的小说项目已经具备这些方向的雏形：长期记忆、滚动大纲、逐章门禁、批次报告、10 agent 审查、P0/P1/P2 修复记录。若要更工程化，下一步应补齐可解析状态文件、统一门禁 schema、自动恢复入口、061-090 滚动细纲。

## 外部参考

- OpenAI：Prompt engineering 文档，强调构建测试和评估套件来监控 prompt 行为。
- OpenAI：A practical guide to building AI agents，面向产品和工程团队总结 agent 逻辑编排、安全和可预测运行。
- OpenAI：Harness engineering，讨论如何把 Codex/agent 接入真实工程上下文、日志、指标和测试。
- Anthropic：Effective context engineering for AI agents，将 context engineering 视为 prompt engineering 的自然演进。
- LangChain：State of Agent Engineering，指出 2026 年组织关注点从是否构建 agent 转向如何可靠、高效、规模化部署。
- Business Insider：Loop engineering 报道，讨论用循环让 AI agent 自动推进任务。

## 编译建议

将本记录编译到 `wiki/concepts.md` 的“驾驭工程”相关条目中，作为“驾驭工程”的相邻概念谱系和当前行业热词参照。
