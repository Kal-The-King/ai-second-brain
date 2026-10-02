import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
MEMORY_FILE = DATA_DIR / "memory.json"
WEB_CACHE_DIR = DATA_DIR / "web_cache"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(WEB_CACHE_DIR, exist_ok=True)

if not MEMORY_FILE.exists():
    MEMORY_FILE.write_text("[]", encoding="utf-8")

APP_NAME = "AI Second Brain Production"
MAX_MEMORY_ITEMS = 1000
DEFAULT_WEB_RESULTS_LIMIT = 10

# Web Search API Keys
BING_SEARCH_KEY = os.getenv("BING_SEARCH_KEY", "")
SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./brain.db")

# Embeddings
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
EMBEDDING_DIMENSION = int(os.getenv("EMBEDDING_DIMENSION", "1536"))
