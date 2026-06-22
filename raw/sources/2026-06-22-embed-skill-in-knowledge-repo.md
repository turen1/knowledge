# 将 personal-llm-wiki skill 内置到知识库仓库

日期：2026-06-22
来源：Codex conversation
敏感级别：private

## 原始内容或摘要

用户询问：是否可以直接把 skill 内置到 Git 仓库中，让其他 agent clone 到哪个文件夹，哪里就是本地知识库。

已执行：

- 将 `personal-llm-wiki` skill 内置到 `G:\knowledge\skills\personal-llm-wiki`。
- 同步修复本机安装版 `C:\Users\Administrator\.codex\skills\personal-llm-wiki`。
- 将 `kb.py` 改为可移植仓库识别：
  1. 优先使用 `PERSONAL_KB_PATH`。
  2. 向上查找同时包含 `.git`、`raw/`、`wiki/` 的目录。
  3. 兜底使用 `G:\knowledge`。
- 验证本机安装版和仓库内置版 skill 均有效。

## 可编译事实

- 其他 agent 可以 clone `git@github.com:turen1/knowledge.git` 到任意目录。
- clone 目录会被 repo-embedded skill 自动识别为知识库根目录。
- 如需 `$personal-llm-wiki` 自动触发，仍需把 `skills/personal-llm-wiki` 复制或链接到该 agent 的 skills 目录，或者让 agent 显式加载该路径。

## 待确认

- 是否需要新增跨平台安装脚本，例如 `install_skill.ps1` 和 `install_skill.sh`。

