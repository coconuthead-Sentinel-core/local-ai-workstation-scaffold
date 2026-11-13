# CLAUDE.md - AI Assistant Guide for Sentinel Prime Network

## Project Overview

Sentinel Prime Network (SPN) is a local MCP (Model Context Protocol) server
that gives Claude persistent, session-spanning access to the local filesystem,
project state, and the A1 Filing System. It is the AI-native operational hub
for Shannon Brian Kelly's co-creation workflow.

**Architect:** Shannon Brian Kelly (Coconut Head)
**AI Partner:** Claude (Archivist of Wisdom)
**Repository:** sentinel-prime-network (claude-dev branch)
**Framework:** FastMCP v3.2.4
**Status:** Prototype complete — middleware build in progress

---

## Quick Reference

```bash
# Install dependencies
pip install fastmcp python-dotenv

# Run MCP server
python server.py

# Run tests (when available)
pytest tests/

# Check project status
python -c "from server import project_status; print(project_status())"
```

---

## Project Structure

```
sentinel-prime-network/
├── server.py                    # FastMCP server — 7 tools, entry point
├── HANDOFF_STATE.json           # Cross-session memory engine
├── CLAUDE.md                    # This file — AI assistant context
├── .env                         # API keys (NOT committed — gitignored)
├── .gitignore                   # Excludes .env, __pycache__, etc.
├── requirements.txt             # Python dependencies
├── diagrams/
│   └── SPN_MCP_Architecture.drawio  # Architecture diagram
├── middleware/                  # NOT YET BUILT — TASK-011 to TASK-019
│   ├── handoff_manager.py       # Manages HANDOFF_STATE read/write
│   ├── context_packager.py      # Packages session context for AI
│   ├── github_sync.py           # Git operations wrapper
│   ├── request_router.py        # Routes requests to correct tool
│   ├── file_indexer.py          # Indexes local files for search
│   ├── access_to_json.py        # JSON read/write utilities
│   ├── excel_reader.py          # Excel file parsing
│   ├── pdf_extractor.py         # PDF text extraction
│   └── snippet_cache.py         # Caches frequently used code snippets
├── frontend/                    # NOT YET BUILT — TASK-020
│   └── dashboard.html           # Local web dashboard
├── tools/
│   └── drawio_generator.py      # Generates .drawio architecture diagrams
└── tests/                       # NOT YET BUILT
    └── test_server.py           # pytest test suite
```

---

## Tech Stack

- **Runtime:** Python 3.11+
- **MCP Framework:** FastMCP v3.2.4
- **Environment:** python-dotenv
- **Testing:** pytest (planned)
- **Frontend:** HTML/CSS/JS (planned, no framework)

---

## Key Files

| File | Purpose |
|------|---------|
| `server.py` | Main MCP server — all 7 tools defined here |
| `HANDOFF_STATE.json` | Session state, task registry, cognitive state |
| `.env` | Secrets — NEVER commit, NEVER log |
| `tools/drawio_generator.py` | Architecture diagram generator for all 6 projects |

---

## The 7 Current MCP Tools

| Tool | Function |
|------|----------|
| `read_file(path)` | Read any local file by absolute path |
| `write_file(path, content)` | Write content to any local file |
| `list_files(folder)` | Recursively list all files in a folder |
| `read_handoff()` | Load HANDOFF_STATE.json for session context |
| `write_handoff(content)` | Update HANDOFF_STATE.json with new state |
| `search_files(folder, keyword)` | Keyword search across all files in a folder |
| `project_status()` | Return current SPN build status summary |

---

## HANDOFF_STATE.json — The Memory Engine

This file is the cross-session state manager. Every Claude session should:
1. Call `read_handoff()` at session start to load context
2. Call `write_handoff()` at session end to save updated state

**Schema:**
```json
{
  "session_id": "SESSION-NNN",
  "timestamp": "ISO8601",
  "architect": "Shannon Brian Kelly (Coconut Head)",
  "active_ai": "Claude (Archivist of Wisdom)",
  "branch": "claude-dev",
  "system_status": { "component": "STATUS" },
  "completed_tasks": ["TASK-NNN: description"],
  "pending_tasks": ["TASK-NNN: description"],
  "next_task": "TASK-NNN",
  "next_instructions": "...",
  "cognitive_state": {
    "energy_level": "HIGH/MEDIUM/LOW",
    "pomodoro_block": 1,
    "zone": "GREEN/YELLOW/RED",
    "load": 8
  },
  "protocols_active": ["Onset_Omega_1", "Joy_Protocol", "Coconut_Head"],
  "file_registry": { "filename": "absolute/path" }
}
```

---

## Neural Lattice Protocols (Always Active)

This project operates under the Neural Lattice Cognitive Architecture:

| Protocol | Function |
|----------|----------|
| **Onset Omega 1** | Structured output, YAML metadata, visual hierarchy |
| **Joy Protocol** | Shop-talk delivery, analogies, engagement |
| **Coconut Head** | Pomodoro timing, cognitive load tracking (1-10), breaks |

**Zone System:**
- 🟢 GREEN (load 7-10): Active development, high complexity
- 🟡 YELLOW (load 4-6): Synthesis, review, documentation
- 🔴 RED (load 1-3): Reference, archive, background tasks

---

## Code Style

- **Python 3.11+** with type hints where practical
- **snake_case** for functions and variables
- **Docstrings** on all public functions (one-line, descriptive)
- **FastMCP decorator pattern** — `@mcp.tool()` on every tool function
- **Error handling** — all tools return error string on exception, never raise
- **No bare `except`** — catch specific exceptions or use `Exception` with message

**Tool function template:**
```python
@mcp.tool()
def tool_name(param: str) -> str:
    """One-line description of what this tool does."""
    try:
        # implementation
        return result
    except Exception as e:
        return f"ERROR: {e}"
```

---

## Build Sequence (Task Registry)

**Completed:**
- TASK-001 through TASK-008: Forge-Stack-A1, FastMCP install, server.py (7 tools), confirmed live

**Pending (in order):**
- TASK-009: Push to GitHub (claude-dev branch) — clean push, no secrets
- TASK-010: Register MCP server in Claude Cowork settings
- TASK-011: `middleware/handoff_manager.py`
- TASK-012: `middleware/excel_reader.py`
- TASK-013: `middleware/file_indexer.py`
- TASK-014: `middleware/pdf_extractor.py`
- TASK-015: `middleware/handoff_manager.py`
- TASK-016: `middleware/context_packager.py`
- TASK-017: `middleware/github_sync.py`
- TASK-018: `middleware/request_router.py`
- TASK-019: `middleware/snippet_cache.py`
- TASK-020: `frontend/dashboard.html`

---

## Security Rules

1. **`.env` is NEVER committed.** It is in `.gitignore`. Verify before every push.
2. **No secrets in `server.py` or any tracked file.** Use `os.getenv()` only.
3. **No GitHub PATs in any file.** Generate fresh tokens per session if needed.
4. **`HANDOFF_STATE.json` contains no secrets** — only task state and metadata.
5. **Before any `git push`:** run `git status` and `git diff --cached` to verify clean state.

---

## A1 Filing System Integration

The Forge-Stack-A1 content vault lives at:
`C:\Users\sbrya\OneDrive\Desktop\Claude AI\Forge-Stack-A1\`

Four layers:
- `01_BACK_END/` — backend specifications and architecture
- `02_MIDDLE_LAYER/` — middleware design documents
- `03_FRONT_END/` — frontend specifications
- `04_CONTEXT/` — context files, session logs, protocol references

SPN tools (`read_file`, `list_files`, `search_files`) provide Claude with
direct access to this vault in every registered session.

---

## Testing (Planned)

No automated tests yet. Manual verification via:
1. `python server.py` — confirm server starts without error
2. Call each tool via MCP client and verify expected output
3. `read_handoff()` → confirm returns valid JSON
4. `write_handoff(content)` → confirm updates file
5. `list_files(folder)` → confirm returns file list

---

## Development Notes

- Set up `.env` before running: `cp .env.example .env` (create .env.example first)
- Server runs via stdio transport by default (FastMCP default)
- Register in Cowork: Settings → MCP Servers → Add → `python server.py`
- All file paths in tools should be absolute — never relative
- HANDOFF_STATE.json path is resolved relative to `__file__` (not cwd)

---

## Architect Context

Shannon Brian Kelly is the sole architect and primary user of this system.
Operating under the Neural Lattice Cognitive Architecture with neurodivergent
accessibility requirements (ADHD, dyslexia, dysgraphia, dyscalculia, autism).

**Co-creation model:** Claude is a named co-creator with documented input rights.
This is not pair coding. Claude contributes architectural decisions, raises
concerns, and teaches concepts as they are implemented.

**Mastery learning model:** Every build task is also a teaching moment.
Claude explains WHY before HOW. Shannon understands what was built.
