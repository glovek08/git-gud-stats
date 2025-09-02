from typing import Union
from fastapi import FastAPI
import httpx

app = FastAPI()

GITHUB_API_URL = "https://api.github.com/users/";

@app.get("/")
def read_root():
    return { "message": "GitHub User Info API" };

@app.get("/user/{username}")
async def get_github_user(username: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{GITHUB_API_URL}{username}");
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="User not found")
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="GitHub API error")
        return response.json()

