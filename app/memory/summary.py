import json
from pathlib import Path


class MemorySummary:
    def __init__(self, memory_store):
        self.memory_store = memory_store

    def create_summary(self):
        items = self.memory_store.list()
        if not items:
            return {"summary": "No memories yet."}

        categories = {}
        for item in items:
            categories.setdefault(item.get("category", "general"), []).append(item.get("text", ""))

        summary = {
            "total_memories": len(items),
            "categories": {key: len(value) for key, value in categories.items()},
            "latest": items[-1]
        }
        return summary
