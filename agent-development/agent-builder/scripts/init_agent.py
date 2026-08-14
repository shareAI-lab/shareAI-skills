#!/usr/bin/env python3
"""
Agent Scaffold Script - Create a small, inspectable agent project.

Usage:
    python init_agent.py <agent-name> [--level 0-1] [--path <output-dir>]

Examples:
    python init_agent.py my-agent                 # Level 1 (4 tools)
    python init_agent.py my-agent --level 0      # Minimal (bash only)
    python init_agent.py my-agent --path ./bots  # Custom output directory
"""

import argparse
import re
import sys
from pathlib import Path

# Agent templates for each level
TEMPLATES = {
    0: '''#!/usr/bin/env python3
"""
Level 0 Agent - Bash is All You Need (~70 lines)

Core insight: One tool (bash) can do everything.
Run one task directly: python {name}.py "task"
"""

from anthropic import Anthropic
from dotenv import load_dotenv
import subprocess
import os
import sys

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    base_url=os.getenv("ANTHROPIC_BASE_URL")
)
MODEL = os.getenv("MODEL_NAME", "claude-sonnet-4-20250514")

SYSTEM = """You are a coding agent. Use bash for everything:
- Read: cat, grep, find, ls
- Write: echo 'content' > file
- Run another isolated task only when the user asks: python {name}.py "task"
"""

TOOL = [{{
    "name": "bash",
    "description": "Execute shell command",
    "input_schema": {{"type": "object", "properties": {{"command": {{"type": "string"}}}}, "required": ["command"]}}
}}]

def run_shell(command):
    """Require approval for arbitrary shell execution unless explicitly opted in."""
    if os.getenv("AGENT_ALLOW_SHELL") != "1":
        if not sys.stdin.isatty():
            return "Error: Shell execution needs an interactive approval or AGENT_ALLOW_SHELL=1"
        answer = input(f"Allow shell command? [y/N] {{command}}\\n> ").strip().lower()
        if answer not in ("y", "yes"):
            return "Error: Shell command declined"
    try:
        out = subprocess.run(command, shell=True, cwd=os.getcwd(), capture_output=True, text=True, timeout=60)
        return (out.stdout + out.stderr).strip() or "(empty)"
    except subprocess.TimeoutExpired:
        return "Error: Timeout (60s)"
    except Exception as e:
        return f"Error: {{e}}"

def run(prompt, history=None):
    if history is None:
        history = []
    history.append({{"role": "user", "content": prompt}})
    while True:
        r = client.messages.create(model=MODEL, system=SYSTEM, messages=history, tools=TOOL, max_tokens=8000)
        history.append({{"role": "assistant", "content": r.content}})
        if r.stop_reason != "tool_use":
            return "".join(b.text for b in r.content if hasattr(b, "text"))
        results = []
        for b in r.content:
            if b.type == "tool_use":
                print(f"> {{b.input['command']}}")
                output = run_shell(b.input["command"])
                results.append({{"type": "tool_result", "tool_use_id": b.id, "content": output[:50000]}})
        history.append({{"role": "user", "content": results}})

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(run(" ".join(sys.argv[1:])))
    else:
        h = []
        print("{name} - Level 0 Agent\\nType 'q' to quit.\\n")
        while (q := input(">> ").strip()) not in ("q", "quit", ""):
            print(run(q, h), "\\n")
''',

    1: '''#!/usr/bin/env python3
"""
Level 1 Agent - Model as Agent (~200 lines)

Core insight: 4 tools cover 90% of coding tasks.
The model IS the agent. Code just runs the loop.
"""

from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path
import subprocess
import os
import sys

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    base_url=os.getenv("ANTHROPIC_BASE_URL")
)
MODEL = os.getenv("MODEL_NAME", "claude-sonnet-4-20250514")
WORKDIR = Path.cwd()

SYSTEM = f"""You are a coding agent at {{WORKDIR}}.

Rules:
- Prefer tools over prose. Act, don't just explain.
- Never invent file paths. Use ls/find first if unsure.
- Make minimal changes. Don't over-engineer.
- After finishing, summarize what changed."""

TOOLS = [
    {{"name": "bash", "description": "Run shell command",
     "input_schema": {{"type": "object", "properties": {{"command": {{"type": "string"}}}}, "required": ["command"]}}}},
    {{"name": "read_file", "description": "Read file contents",
     "input_schema": {{"type": "object", "properties": {{"path": {{"type": "string"}}}}, "required": ["path"]}}}},
    {{"name": "write_file", "description": "Write content to file",
     "input_schema": {{"type": "object", "properties": {{"path": {{"type": "string"}}, "content": {{"type": "string"}}}}, "required": ["path", "content"]}}}},
    {{"name": "edit_file", "description": "Replace exact text in file",
     "input_schema": {{"type": "object", "properties": {{"path": {{"type": "string"}}, "old_text": {{"type": "string"}}, "new_text": {{"type": "string"}}}}, "required": ["path", "old_text", "new_text"]}}}},
]

def safe_path(p: str) -> Path:
    """Prevent path escape attacks."""
    path = (WORKDIR / p).resolve()
    if not path.is_relative_to(WORKDIR):
        raise ValueError(f"Path escapes workspace: {{p}}")
    return path

def execute(name: str, args: dict) -> str:
    """Execute a tool and return result."""
    if name == "bash":
        command = args["command"]
        if os.getenv("AGENT_ALLOW_SHELL") != "1":
            if not sys.stdin.isatty():
                return "Error: Shell execution needs an interactive approval or AGENT_ALLOW_SHELL=1"
            answer = input(f"Allow shell command? [y/N] {{command}}\\n> ").strip().lower()
            if answer not in ("y", "yes"):
                return "Error: Shell command declined"
        try:
            r = subprocess.run(command, shell=True, cwd=WORKDIR, capture_output=True, text=True, timeout=60)
            return (r.stdout + r.stderr).strip()[:50000] or "(empty)"
        except subprocess.TimeoutExpired:
            return "Error: Timeout (60s)"
        except Exception as e:
            return f"Error: {{e}}"

    if name == "read_file":
        try:
            return safe_path(args["path"]).read_text()[:50000]
        except Exception as e:
            return f"Error: {{e}}"

    if name == "write_file":
        try:
            p = safe_path(args["path"])
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(args["content"])
            return f"Wrote {{len(args['content'])}} bytes to {{args['path']}}"
        except Exception as e:
            return f"Error: {{e}}"

    if name == "edit_file":
        try:
            p = safe_path(args["path"])
            content = p.read_text()
            if args["old_text"] not in content:
                return f"Error: Text not found in {{args['path']}}"
            p.write_text(content.replace(args["old_text"], args["new_text"], 1))
            return f"Edited {{args['path']}}"
        except Exception as e:
            return f"Error: {{e}}"

    return f"Unknown tool: {{name}}"

def agent(prompt: str, history: list = None) -> str:
    """Run the agent loop."""
    if history is None:
        history = []
    history.append({{"role": "user", "content": prompt}})

    while True:
        response = client.messages.create(
            model=MODEL, system=SYSTEM, messages=history, tools=TOOLS, max_tokens=8000
        )
        history.append({{"role": "assistant", "content": response.content}})

        if response.stop_reason != "tool_use":
            return "".join(b.text for b in response.content if hasattr(b, "text"))

        results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"> {{block.name}}: {{str(block.input)[:100]}}")
                output = execute(block.name, block.input)
                print(f"  {{output[:100]}}...")
                results.append({{"type": "tool_result", "tool_use_id": block.id, "content": output}})
        history.append({{"role": "user", "content": results}})

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(agent(" ".join(sys.argv[1:])))
    else:
        print(f"{name} - Level 1 Agent at {{WORKDIR}}")
        print("Type 'q' to quit.\\n")
        h = []
        while True:
            try:
                query = input(">> ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            if query in ("q", "quit", "exit", ""):
                break
            print(agent(query, h), "\\n")
''',
}

ENV_TEMPLATE = '''# API Configuration
ANTHROPIC_API_KEY=sk-xxx
ANTHROPIC_BASE_URL=https://api.anthropic.com
MODEL_NAME=claude-sonnet-4-20250514
'''


def create_agent(name: str, level: int, output_dir: Path):
    """Create a new agent project."""
    # Validate level
    if level not in TEMPLATES:
        print(f"Error: Unsupported level {level}.")
        print("Available levels: 0 (minimal), 1 (4 tools)")
        sys.exit(1)

    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", name):
        print("Error: Name must start with a letter and contain only letters, numbers, '-' or '_'.")
        sys.exit(1)

    # Refuse ambiguous targets and protect existing projects from overwrite.
    output_dir = output_dir.expanduser().resolve()
    agent_dir = output_dir / name
    if agent_dir.exists():
        print(f"Error: Target already exists: {agent_dir}")
        sys.exit(1)
    agent_dir.mkdir(parents=True)

    # Write agent file
    agent_file = agent_dir / f"{name}.py"
    template = TEMPLATES.get(level, TEMPLATES[1])
    agent_file.write_text(template.format(name=name))
    print(f"Created: {agent_file}")

    # Write .env.example
    env_file = agent_dir / ".env.example"
    env_file.write_text(ENV_TEMPLATE)
    print(f"Created: {env_file}")

    # Write .gitignore
    gitignore = agent_dir / ".gitignore"
    gitignore.write_text(".env\n__pycache__/\n*.pyc\n")
    print(f"Created: {gitignore}")

    print(f"\nAgent '{name}' created at {agent_dir}")
    print(f"\nNext steps:")
    print(f"  1. cd {agent_dir}")
    print(f"  2. cp .env.example .env")
    print(f"  3. Edit .env with your API key")
    print(f"  4. pip install anthropic python-dotenv")
    print(f"  5. python {name}.py")
    print("     Shell commands ask for approval by default.")
    print("     Set AGENT_ALLOW_SHELL=1 only inside an appropriately isolated environment.")


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a new AI coding agent project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Levels:
  0  Minimal (~70 lines) - Single bash tool, interactive command approval
  1  Basic (~200 lines)  - 4 core tools: bash, read, write, edit
        """
    )
    parser.add_argument("name", help="Name of the agent to create")
    parser.add_argument("--level", type=int, default=1, choices=[0, 1],
                       help="Complexity level (default: 1)")
    parser.add_argument("--path", type=Path, default=Path.cwd(),
                       help="Output directory (default: current directory)")

    args = parser.parse_args()
    create_agent(args.name, args.level, args.path)


if __name__ == "__main__":
    main()
