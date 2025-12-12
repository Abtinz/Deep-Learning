import os
#from jose import jwt
from dotenv import load_dotenv

from fastmcp import FastMCP
from fastmcp.server.auth import BearerAuthProvider
from fastmcp.server.dependencies import get_access_token, AccessToken


from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.requests import Request as StarletteRequest
from starlette.responses import JSONResponse

#from database import NoteRepository

#Its gonna simply load our environment variables from a .env file
load_dotenv()


mcp = FastMCP(
    name="MCP Authentication Service(Note Application)",
    instructions="Authentication service for MCP using OAuth2 and JWT for Secured access to Note Application APIs.",
    version="1.0.0",
)

@mcp.tool()
def retrieve_users_notes() -> str:
    """Retrieve all notes for the user."""
    return "User's notes would be retrieved here."

@mcp.tool()
def add_note(note_content: str) -> str:
    """Add a new note for the user."""
    return f"Note added: {note_content}"

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=8000,
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_methods=["*"],
                allow_headers=["*"],
                allow_credentials=True
            )
        ]
    )