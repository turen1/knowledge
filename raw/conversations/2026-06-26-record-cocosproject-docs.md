# 记录 CocosProject 文档到个人知识库

日期：2026-06-26
来源：Codex conversation
敏感级别：private

## 原始内容或摘要

用户要求使用 `$personal-llm-wiki` 将 `G:\CocosProject\merge.md` 和 `G:\CocosProject\几口酱提示词视频分析报告.md` 记录到个人知识库。

执行时发现默认路径 `G:\knowledge` 只包含部分 `wiki/` 文件，不是完整 Git 仓库，缺少 `.git` 和 `raw/`。为按知识库维护流程审计、提交并推送，从远程 `git@github.com:turen1/knowledge.git` 重新克隆完整仓库到 `G:\knowledge_repo`，并在该 clone 中完成本次更新。

## 可编译事实

- 当前 CocosProject 工作区路径：`G:\CocosProject`。
- 本次记录的原始来源文件：
  - `raw/sources/2026-06-26-ai-coding-models-game-development-comparison.md`
  - `raw/sources/2026-06-26-jikoujiang-ask-before-execute-prompt-video-analysis.md`
- 当前完整知识库 clone 路径：`G:\knowledge_repo`。
- `G:\knowledge` 当前不是完整 Git 仓库，只保留了部分 wiki 文件。

## 待确认

- 是否将默认知识库路径从 `G:\knowledge` 迁移/恢复为完整仓库，或长期改用 `G:\knowledge_repo`。
