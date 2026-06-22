# 创建 personal-llm-wiki skill

日期：2026-06-22
来源：Codex conversation
敏感级别：private

## 原始内容或摘要

用户要求将个人知识库维护流程提炼成一个可复用 Codex skill，便于记录、更新、查询，并在其他 agent 中通用。

已创建本地 skill：

```text
C:\Users\Administrator\.codex\skills\personal-llm-wiki
```

包含：

- `SKILL.md`
- `references/wiki-maintenance.md`
- `scripts/kb.py`
- `agents/openai.yaml`

## 可编译事实

- 用户希望通过 `$personal-llm-wiki` 统一完成个人知识库的记录、更新、查询和同步。
- 个人知识库维护流程已经被封装为 Codex skill。
- skill 路径为 `C:\Users\Administrator\.codex\skills\personal-llm-wiki`。

## 待确认

- 是否需要把该 skill 同步到某个公开/私有插件仓库，方便其他机器安装。

