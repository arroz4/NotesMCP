# AI Sticky Notes (FastMCP Example)

This project is a simple AI-powered sticky notes server built with [FastMCP](https://github.com/microsoft/model-context-protocol) and Python. It allows you to add, read, and summarize notes via MCP tools and resources, and is ready to be containerized and deployed to Azure.

## Features
- Add new notes
- Read all notes
- Get the latest note
- Generate a summary prompt for all notes

##Important locations
- Docker Image(https://hub.docker.com/repository/docker/omarbarrera/stickynotes)
- HTTP MCP Server Connection (https://stickynotes.purplesmoke-3aaf9869.westus2.azurecontainerapps.io/mcp/)

## Project Structure
- `notes.py` — Main application code (MCP server)
- `notes.txt` — Stores all notes (one per line)
- `Dockerfile` — For building and running the app in a container
- `.env` — Environment variables (e.g., `PORT`)

## Quickstart
1. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   # or if using pyproject.toml
   pip install .
   ```
2. **Run locally**
   ```sh
   python notes.py
   ```
3. **Run in Docker**
   ```sh
   docker build -t ai-sticky-notes .
   docker run -p 2004:2004 --env-file .env ai-sticky-notes
   ```

## Azure Deployment
- Push your Docker image to Azure Container Registry or Docker Hub.
- Deploy to Azure Web App for Containers, Azure Container Instances, or AKS.
- Make sure to mount persistent storage if you want to keep notes between restarts.

## Environment Variables
- `PORT` — The port the server listens on (default: 2004)

## License
MIT
