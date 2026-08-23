from urllib.parse import quote_plus


class ShadowDoxEngine:

    def search(self, query):
        query_encoded = quote_plus(query)

        return {
            "query": query,
            "web": [
                {
                    "name": "Google",
                    "url": f"https://www.google.com/search?q={query_encoded}",
                },
                {
                    "name": "Bing",
                    "url": f"https://www.bing.com/search?q={query_encoded}",
                },
                {
                    "name": "DuckDuckGo",
                    "url": f"https://duckduckgo.com/?q={query_encoded}",
                },
            ],
            "social": [
                {
                    "name": "X",
                    "url": f"https://x.com/search?q={query_encoded}",
                },
                {
                    "name": "Instagram",
                    "url": f"https://www.instagram.com/explore/search/keyword/?q={query_encoded}",
                },
                {
                    "name": "LinkedIn",
                    "url": f"https://www.linkedin.com/search/results/all/?keywords={query_encoded}",
                },
            ],
        }
      
