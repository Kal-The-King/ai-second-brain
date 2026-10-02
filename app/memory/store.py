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

    def add(self, text: str):
        items = self._read()
        items.append({
            "id": len(items) + 1,
            "text": text,
            "timestamp": datetime.utcnow().isoformat()
        })
        self._write(items)
        return items[-1]

    def list(self):
        return self._read()

    def search(self, query: str):
        items = self._read()
        query = query.lower()
        return [item for item in items if query in item["text"].lower()]
