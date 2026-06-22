# Personal LLM Wiki

这个仓库是一个按 Karpathy LLM Wiki 思路搭建的个人知识库，用来长期记录“关于我的一切”。

核心原则：

- `raw/` 保存原始资料和事实来源，尽量不可改，只追加。
- `wiki/` 保存由 AI 编译、整理、交叉引用后的 Markdown 知识页。
- 每条关于用户的事实都应能追溯到 `raw/` 或明确的用户指令。
- 不使用向量数据库作为第一层记忆；个人规模优先用可读、可审计、可版本管理的 Markdown。
- 每次更新知识库后必须提交并推送到 GitHub。

远程仓库：

```text
git@github.com:turen1/knowledge.git
```

## 目录

```text
raw/          原始资料、对话摘要、导入文档、事实来源
wiki/         编译后的个人知识库
templates/    新资料、新人物、新项目等模板
scripts/      辅助审计和维护脚本
```

## 使用方式

1. 把新资料放入 `raw/`，不要直接覆盖旧资料。
2. 让 Codex/LLM 按 `AGENTS.md` 规则更新 `wiki/`。
3. 运行审计：

```powershell
python scripts/audit_kb.py
```

4. 提交并推送：

```powershell
git add .
git commit -m "Update knowledge base"
git push
```

## 初始来源

本仓库根据 Karpathy 的 LLM Wiki 方案初始化：

- 原始 gist：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

