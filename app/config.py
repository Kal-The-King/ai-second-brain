import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
MEMORY_FILE = DATA_DIR / "memory.json"
WEB_CACHE_DIR = DATA_DIR / "web_cache"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(WEB_CACHE_DIR, exist_ok=True)

if not MEMORY_FILE.exists():
    MEMORY_FILE.write_text("[]", encoding="utf-8")

APP_NAME = "AI Second Brain Advanced"
MAX_MEMORY_ITEMS = 500
DEFAULT_WEB_RESULTS_LIMIT = 5
