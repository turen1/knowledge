# Personal Knowledge Base Maintenance

## Repository

```text
git@github.com:turen1/knowledge.git
```

The local repository can be any clone path. The helper finds the repo root from `PERSONAL_KB_PATH` or by walking up from the skill directory.

## Page Map

- `wiki/index.md`: entry point.
- `wiki/profile.md`: durable user identity and high-level profile.
- `wiki/preferences.md`: communication, work, quality, tool, and style preferences.
- `wiki/projects.md`: active and historical projects.
- `wiki/workflows.md`: repeated procedures and operating patterns.
- `wiki/concepts.md`: concepts, methods, terminology.
- `wiki/tools.md`: software, local paths, machines, accounts, environments.
- `wiki/timeline.md`: dated events.
- `wiki/open-questions.md`: unknowns and facts needing confirmation.
- `wiki/provenance.md`: source index.

## Source File Naming

Use dated names:

```text
raw/conversations/YYYY-MM-DD-topic.md
raw/projects/YYYY-MM-DD-project.md
raw/sources/YYYY-MM-DD-source.md
```

## Commit Policy

Every knowledge update must end with:

```powershell
python scripts\audit_kb.py
git status --short
git add .
git commit -m "..."
git push
```

