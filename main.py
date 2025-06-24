# server.py
from mcp.server.fastmcp import FastMCP
import os

#create mcp server
mcp = FastMCP("notes")

Notes_file = os.path.join(os.path.dirname(__file__),"notes.txt")

def ensure_file():
    if not os.path.exists(Notes_file):
        with open(Notes_file, "w") as f:
            f.write("")


@mcp.tool()
def make_notes(message: str) -> str:
    """
    Append a new note to the note file.

    Args:
        message(str): the note content to be added

    Returns:
        str:Confirmation message indicating message was saved.
    """
    ensure_file()
    with open(Notes_file, "a") as f:
        f.write(message + "\n")
    return "Notes Saved"

@mcp.tool()
def read_notes()->str:
    """
    Reads and returns all the content from the note file

    Returns:
        str:All notes in a single string seperated by lines.
        if no notes exist, defaukt message is shown
    """
    ensure_file()
    with open(Notes_file,"r") as f:
        content = f.read().strip()
    return content or "No notes yet"


@mcp.resource("notes://latest")
def get_latest_notes() -> str:
    ensure_file()
    with open(Notes_file, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines[-1] if lines else "No notes yet"


@mcp.tool()
def summarize_notes()->str:
    ensure_file()
    with open(Notes_file,"r") as f:
        content = f.read().strip()
    if not content:
        return "No notes yet"
    return f"Summarize the notes: {content}"

@mcp.tool()
def clear_notes() -> str:
    with open(Notes_file, "w") as f:
        f.write("")
    return "All notes cleared."
