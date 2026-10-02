import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
MEMORY_FILE = DATA_DIR / "memory.json"

os.makedirs(DATA_DIR, exist_ok=True)

if not MEMORY_FILE.exists():
    MEMORY_FILE.write_text("[]", encoding="utf-8")

APP_NAME = "AI Second Brain"
MAX_MEMORY_ITEMS = 100
