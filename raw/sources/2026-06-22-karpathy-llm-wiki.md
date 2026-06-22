# Karpathy LLM Wiki 方案

来源链接：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

采集日期：2026-06-22

## 摘要

Karpathy 的 LLM Wiki 思路是把个人或项目知识库分成两层：

- `raw/`：保存原始资料，作为不可随意改写的事实来源。
- `wiki/`：由 LLM 从 `raw/` 编译出的结构化、互链 Markdown 知识库。

这种模式强调“知识编译”而不是每次临时 RAG 检索。知识会在 Markdown 中累积、交叉引用和持续改进。

## 本仓库采用的原则

- 原始资料先进入 `raw/`。
- 编译后的个人事实写入 `wiki/`。
- 每条关键事实尽量保留来源。
- 用 Git 记录每次知识库更新。
- 每次更新后推送到 GitHub。

