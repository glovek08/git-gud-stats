import httpx


class GithubClient:
    BASE_URL = "https://api.github.com/graphql"

    def __init__(self, token: str):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github.v4+json",
            "User-Agent": "git-gud-stats",
        }

    async def execute_query(self, query: str, variables: dict = {}) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.BASE_URL,
                json={"query": query, "variables": variables},
                headers=self.headers,
                timeout=10.0,
            )

        response.raise_for_status()

        return response.json()
