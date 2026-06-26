# 恢复默认知识库路径

日期：2026-06-26
来源：Codex conversation
敏感级别：private

## 原始内容或摘要

用户要求恢复 `G:\knowledge` 为默认完整知识库，并继续查询多 agent 协作开发相关知识。

执行前检查发现 `G:\knowledge` 当前不存在，`G:\knowledge_repo` 是完整且已推送到 GitHub 的临时 clone，远程 `git@github.com:turen1/knowledge.git` 的 HEAD 为 `f4368cd`。随后从远程仓库重新 clone 到 `G:\knowledge`，恢复默认路径。

## 可编译事实

- 默认知识库路径 `G:\knowledge` 已恢复为完整 Git 仓库。
- `G:\knowledge` 当前包含 `.git`、`raw/`、`wiki/`、`scripts/`、`skills/`、`templates/`。
- 恢复后审计通过：`python scripts\audit_kb.py`。
- `G:\knowledge_repo` 仍可作为历史临时 clone，但默认路径应回到 `G:\knowledge`。

## 待确认

- 是否删除或保留 `G:\knowledge_repo` 这个临时 clone。
