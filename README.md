# AI Second Brain Advanced

This version adds:
- richer memory categories
- web content caching
- web knowledge hooks
- easier extension for semantic search and agent memory

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
brain.store_memory("The user prefers structured answers.", category="preferences")
print(brain.reply("What kind of responses do I prefer?"))
```
