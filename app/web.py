import json
from pathlib import Path

from app.config import WEB_CACHE_DIR


class WebMemory:
    def __init__(self, cache_dir: str | Path = WEB_CACHE_DIR):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def save_page(self, url: str, content: str):
        path = self.cache_dir / (url.replace("https://", "").replace("http://", "").replace("/", "_") + ".txt")
        path.write_text(content, encoding="utf-8")
        return {"url": url, "path": str(path)}

    def list_cached_pages(self):
        return [p.name for p in self.cache_dir.iterdir() if p.is_file()]


class WebKnowledge:
    def __init__(self, web_memory: WebMemory | None = None):
        self.web_memory = web_memory or WebMemory()

    def fetch(self, url: str, content: str):
        return self.web_memory.save_page(url, content)

    def summarize(self, content: str):
        sentences = [s.strip() for s in content.split(".") if s.strip()]
        return " ".join(sentences[:3])
