# 时间线

## 2026-06-22

- 用户要求按 Karpathy LLM Wiki 方案搭建个人知识库。
- 用户指定 GitHub 仓库：`git@github.com:turen1/knowledge.git`。
- 用户要求每次更新知识库后推送到 GitHub。
- 初始化本地仓库 `G:\knowledge`。
- 将个人知识库维护流程封装为 Codex skill：`personal-llm-wiki`。
- 记录“驾驭工程”和“提示词工程”的区别，并编译到概念库。
- 将 `personal-llm-wiki` skill 内置到知识库仓库，并改造成 clone 路径自识别。

来源：`raw/conversations/2026-06-22-initial-context.md`
来源：`raw/sources/2026-06-22-personal-llm-wiki-skill.md`
来源：`raw/conversations/2026-06-22-driving-engineering-vs-prompt-engineering.md`
来源：`raw/sources/2026-06-22-embed-skill-in-knowledge-repo.md`

## 2026-06-24

- 记录当前热门 AI/LLM 工程方向，并将上下文工程、智能体工程、循环工程、Harness Engineering、评测工程、RAG/知识库工程、记忆工程、工具/MCP 工程、可靠性与安全工程、多 agent 协同工程关联到“驾驭工程”概念。

来源：`raw/conversations/2026-06-24-current-hot-ai-engineering-fields.md`

## 2026-06-26

- 记录 `merge.md`，沉淀 Claude、Codex、Gemini 在游戏开发中的分工协作策略。
- 记录《几口酱聊AI：先提问再执行提示词方法论》分析报告，沉淀“先提问，再执行”、Best Minds、GStack / Office Hours 等提示词方法论。
- 因 `G:\knowledge` 不是完整 Git 仓库，重新从 `git@github.com:turen1/knowledge.git` 克隆完整知识库到 `G:\knowledge_repo` 进行本次维护。
- 恢复默认知识库路径：从远程 `git@github.com:turen1/knowledge.git` 重新 clone 到 `G:\knowledge`，并确认审计通过。

来源：`raw/conversations/2026-06-26-record-cocosproject-docs.md`
来源：`raw/conversations/2026-06-26-restore-default-knowledge-path.md`
来源：`raw/sources/2026-06-26-ai-coding-models-game-development-comparison.md`
来源：`raw/sources/2026-06-26-jikoujiang-ask-before-execute-prompt-video-analysis.md`
