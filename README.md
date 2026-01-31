# AI Media Filter

A Python-based tool to help analyze and organize image/media AI files by scanning folders, extracting basic file metadata, and generating a structured output. This project is being developed iteratively with a focus on clean structure, documentation, and testability.

## Why this exists
I wanted a repeatable way to review and organize large media folders without manually opening files one-by-one. The goal is to automate the organizing step (scan → label → report) so I can filter or route AI files into categories efficiently.

## Current Features
- Scans a folder recursively for media files
- Filters by allowed extensions (configurable)
- Produces a simple report (counts + file list)
- Provides a CLI entry point

## Planned / Roadmap
- Add configurable categorization rules (by filename patterns, metadata, model output, etc.)
- Add optional ML-based tagging/classification
- Export results to CSV/JSON
- Add performance improvements for large folders
- Adding a GUI function


## Requirements
- Python 3.10+ recommended

## Installation
Create a virtual environment (recommended), then install your dependencies.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements-dev.txt
