from app.memory.manager import MemoryManager


class SecondBrain:
    def __init__(self, memory_manager: MemoryManager | None = None):
        self.memory_manager = memory_manager or MemoryManager()

    def store_memory(self, text: str, category: str = "general", source: str | None = None, tags: list[str] | None = None):
        return self.memory_manager.save(text, category=category, source=source, tags=tags)

    def retrieve_memory(self, query: str):
        return self.memory_manager.recall(query)

    def list_memory(self):
        return self.memory_manager.all()

    def summarize_memory(self):
        memories = self.list_memory()
        if not memories:
            return "No memory saved yet."

        summary_lines = []
        for item in memories[-5:]:
            category = item.get("category", "general")
            text = item.get("text", "")
            summary_lines.append(f"[{category}] {text}")
        return "\n".join(summary_lines)

    def reply(self, user_message: str):
        memories = self.retrieve_memory(user_message)
        if memories:
            context = "\n".join(f"- {m['text']} (score: {m.get('score', 0)})" for m in memories[:5])
            return f"Relevant memory:\n{context}\n\nResponse to: {user_message}"
        return f"No memory match found. I can store this and use it later: {user_message}"
