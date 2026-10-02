from typing import List, Optional
from app.db import SessionLocal, WebCache
from app.services.web_service import WebSearchService, PageFetcher, Summarizer


class WebBrain:
    def __init__(self, bing_key: str = None):
        self.db = SessionLocal()
        self.search_service = WebSearchService(bing_key)
        self.fetcher = PageFetcher()
        self.summarizer = Summarizer()

    def search_and_cache(self, query: str, limit: int = 5) -> List[dict]:
        results = self.search_service.search(query, count=limit)
        cached_results = []
        
        for result in results:
            cached = self.db.query(WebCache).filter(WebCache.url == result["url"]).first()
            if cached:
                cached_results.append({
                    "url": result["url"],
                    "title": result["title"],
                    "snippet": result["snippet"],
                    "cached": True
                })
            else:
                content = self.fetcher.fetch(result["url"])
                if content:
                    summary = self.summarizer.summarize(content)
                    web_cache = WebCache(
                        id=str(hash(result["url"])),
                        url=result["url"],
                        content=content,
                        summary=summary
                    )
                    self.db.add(web_cache)
                    cached_results.append({
                        "url": result["url"],
                        "title": result["title"],
                        "snippet": result["snippet"],
                        "summary": summary,
                        "cached": True
                    })
        
        self.db.commit()
        return cached_results

    def get_cached(self, url: str) -> Optional[dict]:
        cached = self.db.query(WebCache).filter(WebCache.url == url).first()
        if cached:
            return {"url": url, "content": cached.content, "summary": cached.summary}
        return None
