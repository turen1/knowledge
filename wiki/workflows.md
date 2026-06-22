# 常用工作流

## 交接文档驱动任务

模式：

1. 用户提供 `交接_Codex_*.md` 文档。
2. Codex 读取文档和项目目录。
3. Codex 按文档执行任务。
4. Codex 运行校验。
5. Codex 汇报产物路径、统计和异常。

来源：`raw/conversations/2026-06-22-initial-context.md`

## LLM Wiki 知识库更新

模式：

1. 新事实先写入 `raw/`。
2. 更新 `wiki/` 中受影响页面。
3. 更新 `wiki/provenance.md`。
4. 运行 `python scripts/audit_kb.py`。
5. `git add .`
6. `git commit`
7. `git push`

来源：`raw/sources/2026-06-22-karpathy-llm-wiki.md`

## 通过 skill 操作个人知识库

用户希望把个人知识库维护流程封装成通用 skill。当前可用的 skill 是 `$personal-llm-wiki`，支持记录、查询、编译 wiki、审计、提交和推送。

本地路径：

```text
C:\Users\Administrator\.codex\skills\personal-llm-wiki
```

来源：`raw/sources/2026-06-22-personal-llm-wiki-skill.md`
