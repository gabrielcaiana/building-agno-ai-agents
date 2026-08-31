# Repository Guidelines

## Project Structure & Module Organization
This repository is a small Python package managed with `uv`. Core source files live in `src/building_agno_ai_agents/` and are currently organized as numbered example scripts such as `0.llm_call.py`, `1.1.researcher.py`, and `1.5.youtube_assistent.py`. Shared package exports belong in `src/building_agno_ai_agents/__init__.py`. Project metadata and dependencies are defined in `pyproject.toml`, and environment templates live in `.env.sample`.

## Build, Test, and Development Commands
Use `uv` for all local workflows:

- `uv sync`: install and lock dependencies into the local environment.
- `uv run python src/building_agno_ai_agents/0.llm_call.py`: run a specific example script.
- `uv run python src/building_agno_ai_agents/1.1.researcher.py`: run the Tavily-backed research agent.
- `uv run python -m compileall src`: quick syntax validation across the package.

Copy `.env.sample` to `.env` and fill in required API keys before running agents that call Groq, OpenAI, Tavily, or YouTube-related tools.

## Coding Style & Naming Conventions
Target Python 3.11+ and follow PEP 8 with 4-space indentation. Prefer explicit imports, short module-level setup, and concise docstrings for non-obvious functions. Existing files use example-oriented names with numeric prefixes; keep that pattern for tutorial scripts, for example `1.6.new_agent.py`. Use `snake_case` for functions and variables, `PascalCase` for classes, and keep comments brief and instructional.

## Testing Guidelines
There is no dedicated `tests/` directory yet. For now, validate changes by running the affected script with `uv run python ...` and by checking syntax with `uv run python -m compileall src`. When adding reusable logic, introduce `pytest` tests under `tests/` with filenames like `test_researcher.py` and keep network-dependent behavior behind mocks where practical.

## Commit & Pull Request Guidelines
Recent commits use short, imperative summaries such as `create own tools` and `config project setup`. Keep commit messages concise, lowercase is acceptable, and scope each commit to one logical change. Pull requests should include: a brief description, the scripts or modules touched, required environment variables, and terminal output or screenshots when behavior changes are user-visible.

## Security & Configuration Tips
Never commit real secrets from `.env`. Keep `.env.sample` up to date when adding new required variables, and prefer reading credentials through `python-dotenv` rather than hardcoding them in scripts.
