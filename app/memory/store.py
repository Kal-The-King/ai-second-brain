import json
from datetime import datetime
from pathlib import Path

from app.config import MEMORY_FILE


class MemoryStore:
    def __init__(self, file_path: str | Path = MEMORY_FILE):
        self.file_path = Path(file_path)

    def _read(self):
        try:
            return json.loads(self.file_path.read_text(encoding="utf-8"))
        except Exception:
            return []

    def _write(self, data):
        self.file_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def add(self, text: str, category: str = "general", source: str | None = None, tags: list[str] | None = None):
        items = self._read()
        item = {
            "id": len(items) + 1,
            "text": text,
            "category": category,
            "source": source or "user",
            "tags": tags or [],
            "timestamp": datetime.utcnow().isoformat()
        }
        items.append(item)
        self._write(items)
        return item

    def list(self):
        return self._read()

    def search(self, query: str):
        items = self._read()
        q = query.lower()
        ranked = []
        for item in items:
            text = item.get("text", "")
            score = 0
            if q in text.lower():
                score += 2
            if any(q in tag.lower() for tag in item.get("tags", [])):
                score += 3
            if item.get("category", "").lower() == q:
                score += 1
            if score:
                ranked.append({**item, "score": score})
        ranked.sort(key=lambda x: x["score"], reverse=True)
        return ranked

    def clear(self):
        self._write([])
