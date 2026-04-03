# MCP

This folder contains your Model Context Protocol (MCP) work.

## What MCP Means Here

- MCP (Model Context Protocol) is a standard way for models/agents to discover and call tools over a structured interface.
- In this repository, MCP is used to expose backend capabilities as callable tools over HTTP.
- It supports building secure, tool-driven AI systems where model actions are routed through server-defined operations.

## Core Concepts Implemented

- FastMCP server setup and tool registration.
- HTTP transport for MCP tool serving.
- Auth-oriented scaffolding (Bearer/OAuth-style imports and flow structure).
- Middleware-based request handling (CORS).

## Project In This Folder

- `Authentiation/main.py`
  - FastMCP service bootstrap.
  - Exposed tools:
    - `retrieve_users_notes`
    - `add_note`
  - Local HTTP server run configuration and middleware setup.

## Technologies Referenced

- FastMCP
- Starlette middleware/CORS
- dotenv-based environment configuration

