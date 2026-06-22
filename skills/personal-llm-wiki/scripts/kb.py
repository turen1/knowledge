# -*- coding: utf-8 -*-
import argparse
import datetime as dt
import os
import re
import subprocess
import sys
from pathlib import Path


def discover_kb() -> Path:
    env_path = os.environ.get("PERSONAL_KB_PATH")
    if env_path:
        return Path(env_path).expanduser().resolve()

    here = Path(__file__).resolve()
    for parent in [here.parent, *here.parents]:
        if (parent / ".git").exists() and (parent / "raw").exists() and (parent / "wiki").exists():
            return parent

    return Path(r"G:\knowledge")


KB = discover_kb()


def run(cmd, *, check=True):
    return subprocess.run(
        cmd,
        cwd=str(KB),
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=check,
    )


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[\\/:*?\"<>|]+", "-", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:60] or "note"


def ensure_repo():
    if not KB.exists():
        raise SystemExit(f"knowledge repo not found: {KB}")
    if not (KB / ".git").exists():
        raise SystemExit(f"not a git repo: {KB}")
    if not (KB / "raw").exists() or not (KB / "wiki").exists():
        raise SystemExit(f"not a personal LLM Wiki repo: {KB}")


def cmd_status(_args):
    ensure_repo()
    print(f"KB={KB}")
    result = run(["git", "status", "--short", "--branch"])
    sys.stdout.write(result.stdout)


def cmd_query(args):
    ensure_repo()
    result = run(["rg", "-n", "-S", args.term, "wiki", "raw"], check=False)
    if result.stdout:
        sys.stdout.write(result.stdout)
    if result.stderr:
        sys.stderr.write(result.stderr)
    return result.returncode


def cmd_record(args):
    ensure_repo()
    date = args.date or dt.date.today().isoformat()
    folder = KB / "raw" / args.kind
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{date}-{slugify(args.title)}.md"
    if path.exists() and not args.append:
        raise SystemExit(f"source already exists, use --append: {path}")
    block = (
        f"# {args.title}\n\n"
        f"日期：{date}\n"
        f"来源：{args.source}\n"
        f"敏感级别：{args.sensitivity}\n\n"
        "## 原始内容或摘要\n\n"
        f"{args.content.strip()}\n\n"
        "## 可编译事实\n\n"
        "- \n\n"
        "## 待确认\n\n"
        "- \n"
    )
    if args.append:
        with path.open("a", encoding="utf-8") as f:
            f.write("\n---\n\n" + block)
    else:
        path.write_text(block, encoding="utf-8")
    print(path)


def cmd_audit(_args):
    ensure_repo()
    result = run([sys.executable, "scripts\\audit_kb.py"], check=False)
    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)
    return result.returncode


def cmd_push(args):
    ensure_repo()
    audit_code = cmd_audit(args)
    if audit_code != 0:
        return audit_code
    status = run(["git", "status", "--short"])
    if not status.stdout.strip():
        print("No changes to commit.")
        return 0
    run(["git", "add", "."])
    commit = run(["git", "commit", "-m", args.message], check=False)
    sys.stdout.write(commit.stdout)
    sys.stderr.write(commit.stderr)
    if commit.returncode != 0:
        return commit.returncode
    pushed = run(["git", "push"], check=False)
    sys.stdout.write(pushed.stdout)
    sys.stderr.write(pushed.stderr)
    return pushed.returncode


def main():
    parser = argparse.ArgumentParser(description="Operate the personal LLM Wiki")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("status")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("query")
    p.add_argument("term")
    p.set_defaults(func=cmd_query)

    p = sub.add_parser("record")
    p.add_argument("--title", required=True)
    p.add_argument("--content", required=True)
    p.add_argument("--kind", default="conversations", choices=["conversations", "projects", "sources", "personal"])
    p.add_argument("--source", default="user")
    p.add_argument("--sensitivity", default="private", choices=["public", "private", "sensitive"])
    p.add_argument("--date")
    p.add_argument("--append", action="store_true")
    p.set_defaults(func=cmd_record)

    p = sub.add_parser("audit")
    p.set_defaults(func=cmd_audit)

    p = sub.add_parser("push")
    p.add_argument("--message", default="Update personal knowledge base")
    p.set_defaults(func=cmd_push)

    args = parser.parse_args()
    result = args.func(args)
    raise SystemExit(result or 0)


if __name__ == "__main__":
    main()

