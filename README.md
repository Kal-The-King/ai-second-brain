# AI Second Brain

A lightweight modular second-brain system for AI agents.

## Features
- Memory storage
- Searchable memory recall
- Simple chat endpoint
- Easy to plug into other projects

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Example

```python
from app.brain import SecondBrain

brain = SecondBrain()
brain.store_memory("The user prefers concise answers.")
print(brain.reply("What do I prefer?"))
```
