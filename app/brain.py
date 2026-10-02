from app.memory.manager import MemoryManager


class SecondBrain:
    def __init__(self, memory_manager: MemoryManager | None = None):
        self.memory_manager = memory_manager or MemoryManager()

    def store_memory(self, text: str):
        return self.memory_manager.save(text)

    def retrieve_memory(self, query: str):
        return self.memory_manager.recall(query)

    def list_memory(self):
        return self.memory_manager.all()

    def reply(self, user_message: str):
        memories = self.retrieve_memory(user_message)
        context = ""
        if memories:
            context = "\n".join(f"- {m['text']}" for m in memories[:5])
            return f"I found relevant memory:\n{context}\n\nResponse to: {user_message}"
        return f"No saved memory found. I can remember this: {user_message}"
