---
name: personal-llm-wiki
description: Maintain, update, record, and query the user's personal LLM Wiki knowledge base backed by git@github.com:turen1/knowledge.git. Use when the user asks to remember something about them, update personal knowledge, record facts/preferences/projects, search/query the personal knowledge base, summarize what is known about the user, sync/push knowledge updates to GitHub, or install this skill for another agent.
---

# Personal LLM Wiki

Use this skill to operate the user's personal knowledge base.

Default repository:

```text
G:\knowledge
origin: git@github.com:turen1/knowledge.git
```

Portable repository layout:

```text
knowledge/
  raw/
  wiki/
  scripts/
  skills/personal-llm-wiki/
```

The repository follows the Karpathy LLM Wiki pattern:

- `raw/`: original sources, append-first, preserve provenance.
- `wiki/`: AI-compiled Markdown pages.
- `scripts/audit_kb.py`: repository audit.
- `AGENTS.md`: canonical repo-local maintenance rules.

## Repository Discovery

The helper script discovers the knowledge base in this order:

1. `PERSONAL_KB_PATH` environment variable.
2. The nearest parent directory containing `.git`, `raw/`, and `wiki/`.
3. Fallback path `G:\knowledge`.

This means other agents can clone `git@github.com:turen1/knowledge.git` anywhere; when using the repo-embedded skill at `skills/personal-llm-wiki`, that clone directory is the local knowledge base.

## Core Rule

For every update:

1. Write the user's new fact/source into `raw/` first.
2. Update affected pages in `wiki/`.
3. Run `python scripts\audit_kb.py`.
4. Commit and push to GitHub.

Never invent personal facts. Put uncertain items in `wiki/open-questions.md`.

## Quick Commands

Use the bundled helper from either the installed skill or the repo-embedded skill:

```powershell
python "...\personal-llm-wiki\scripts\kb.py" status
python "...\personal-llm-wiki\scripts\kb.py" query "关键词"
python "...\personal-llm-wiki\scripts\kb.py" record --title "标题" --content "内容"
python "...\personal-llm-wiki\scripts\kb.py" push --message "Update knowledge base"
```

The helper only automates raw recording, search, audit, commit, and push. The agent must still edit `wiki/` intelligently when facts should be compiled.

## Installing For Another Agent

Preferred install:

1. Clone the knowledge repo anywhere.
2. Copy or symlink `skills/personal-llm-wiki` into that agent's skills directory.
3. Use `$personal-llm-wiki`.

Example:

```powershell
git clone git@github.com:turen1/knowledge.git D:\knowledge
Copy-Item -Recurse D:\knowledge\skills\personal-llm-wiki $env:USERPROFILE\.codex\skills\
```

If the agent can load a skill by explicit path, it can use the repo copy directly:

```text
D:\knowledge\skills\personal-llm-wiki\SKILL.md
```

## Task Workflows

### Record Something

When the user says "记住", "记录", "更新知识库", or gives personal facts:

1. Use `kb.py record` or create a dated file under `raw/conversations/`.
2. Update relevant wiki pages:
   - identity/profile facts: `wiki/profile.md`
   - preferences: `wiki/preferences.md`
   - projects: `wiki/projects.md`
   - workflows: `wiki/workflows.md`
   - tools/environment: `wiki/tools.md`
   - dated events: `wiki/timeline.md`
   - uncertain facts: `wiki/open-questions.md`
   - source map: `wiki/provenance.md`
3. Run audit.
4. Commit and push.

### Query Knowledge

When the user asks "我之前说过什么", "查一下我的知识库", "关于我你知道什么":

1. Use `kb.py query "term"` or `rg` inside the knowledge repo.
2. Prefer answers from `wiki/` first.
3. Use `raw/` to verify provenance or resolve ambiguity.
4. Cite local file paths in the response when useful.
5. Do not commit if no files changed.

### Compile Raw Into Wiki

When raw files exist but wiki pages are stale:

1. Read new/changed `raw/` files.
2. Edit only affected `wiki/` pages.
3. Keep facts concise and source-backed: `来源：raw/...`.
4. Update `wiki/provenance.md`.
5. Audit, commit, push.

### Sensitive Information

Before adding highly sensitive facts such as health, finance, passwords, legal matters, family details, or exact location:

- If the user explicitly asked to remember that exact information, record it.
- Otherwise ask for confirmation.
- Never record passwords, tokens, API keys, or one-time codes.

## References

Read `references/wiki-maintenance.md` when handling a non-trivial update or when another agent needs the full page map.

