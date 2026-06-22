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

## 在其他 agent 中安装 personal-llm-wiki

推荐方式：

1. 在目标机器或目标 agent 可访问的位置 clone 仓库：

```powershell
git clone git@github.com:turen1/knowledge.git D:\knowledge
```

2. 将仓库内置 skill 复制或链接到该 agent 的 skills 目录：

```powershell
Copy-Item -Recurse D:\knowledge\skills\personal-llm-wiki $env:USERPROFILE\.codex\skills\
```

3. 之后使用 `$personal-llm-wiki`。

如果 agent 支持显式加载 skill 路径，也可以直接使用：

```text
D:\knowledge\skills\personal-llm-wiki\SKILL.md
```

`kb.py` 会自动从 skill 所在目录向上查找 `.git`、`raw/`、`wiki/`，因此 clone 到哪里，哪里就是本地知识库根目录。

来源：`raw/sources/2026-06-22-embed-skill-in-knowledge-repo.md`
