"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""


from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create an MCP server
mcp = FastMCP("AI Sticky Notes",host="0.0.0.0", port=2004)

# Update NOTES_FILE to use the environment variable
NOTES_FILE = os.getenv("NOTES_FILE", os.path.join(os.path.dirname(__file__), "notes.txt"))

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE , "w", encoding="utf-8") as f:
            f.write("")

@mcp.tool()
def add_note(message:str) -> str:
    """
    Append a new note to the sticky note file

    Args:
    message(str) : The note content to be added

    Returns (str):
    Confirmation message indicating note was saved

    """
    ensure_file()
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")
    return "Note saved!"

@mcp.tool()
def read_notes()->str:
    """
    Read and return all notes from the sticky note file.
    Returns(str):
    All notes as a single string separated by line breaks
    If no notes exist, a default message is returned "No notes available"

    """
    ensure_file()
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        content = f.read().strip()
    return content or "No notes yet"

@mcp.resource("notes://latest")
def get_latest_note()->str:
    ensure_file()
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes yet"

@mcp.prompt()
def note_summary_prompt() ->str:
    """
    Generate a prompt asking the AI to summarize all current notes
    Returns(str):
    A prompt string that includes all notes and asks for a summary
    """
    ensure_file()
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        content = f.read().strip()
    if not content:
        return "No notes yet"
    return f"Summarize the current notes {content}"



if __name__ == "__main__":
    # Start the MCP server
    mcp.run(transport="streamable-http")
