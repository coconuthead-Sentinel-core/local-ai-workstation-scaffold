"""
Sentinel Prime Network — MCP Server
Architect: Shannon Brian Kelly (Coconut Head)
AI: Claude (Archivist of Wisdom)
"""

from fastmcp import FastMCP
from dotenv import load_dotenv
import os

load_dotenv()

mcp = FastMCP("Sentinel Prime Network")

# ── TOOL 1: Read a local file ──────────────────────────────────────
@mcp.tool()
def read_file(path: str) -> str:
    """Read any local file and return its contents."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"ERROR: {e}"

# ── TOOL 2: Write a local file ─────────────────────────────────────
@mcp.tool()
def write_file(path: str, content: str) -> str:
    """Write content to a local file."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"SUCCESS: Written to {path}"
    except Exception as e:
        return f"ERROR: {e}"

# ── TOOL 3: List files in a folder ────────────────────────────────
@mcp.tool()
def list_files(folder: str) -> str:
    """List all files in a folder."""
    try:
        results = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                results.append(os.path.join(root, file))
        return "\n".join(results) if results else "No files found."
    except Exception as e:
        return f"ERROR: {e}"

# ── TOOL 4: Read HANDOFF_STATE ────────────────────────────────────
@mcp.tool()
def read_handoff() -> str:
    """Read the current HANDOFF_STATE.json for session context."""
    path = os.path.join(os.path.dirname(__file__), "HANDOFF_STATE.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"ERROR: {e}"

# ── TOOL 5: Write HANDOFF_STATE ───────────────────────────────────
@mcp.tool()
def write_handoff(content: str) -> str:
    """Update HANDOFF_STATE.json with new session state."""
    path = os.path.join(os.path.dirname(__file__), "HANDOFF_STATE.json")
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return "SUCCESS: HANDOFF_STATE.json updated."
    except Exception as e:
        return f"ERROR: {e}"

# ── TOOL 6: Search files for keyword ─────────────────────────────
@mcp.tool()
def search_files(folder: str, keyword: str) -> str:
    """Search all files in a folder for a keyword."""
    try:
        matches = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        if keyword.lower() in f.read().lower():
                            matches.append(filepath)
                except:
                    pass
        return "\n".join(matches) if matches else "No matches found."
    except Exception as e:
        return f"ERROR: {e}"

# ── TOOL 7: Get project status ────────────────────────────────────
@mcp.tool()
def project_status() -> str:
    """Return current Sentinel Prime Network build status."""
    return """
SENTINEL PRIME NETWORK — STATUS
================================
Repo:           LIVE ✅
Forge-Stack-A1: COMPLETE ✅
FastMCP:        INSTALLED ✅
server.py:      RUNNING ✅
Middleware:     NOT STARTED ⏳
Frontend:       NOT STARTED ⏳
MCP registered: NOT STARTED ⏳

Next task: middleware modules
"""

# ── ENTRY POINT ───────────────────────────────────────────────────
if __name__ == "__main__":
    mcp.run()
