from typing import Optional, Dict
from fastapi import FastAPI, HTTPException, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.openapi.utils import get_openapi
import os
import httpx
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
# CORS for a Svelte dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

bearer_scheme = HTTPBearer(auto_error=False)
GITHUB_API_URL = "https://api.github.com/users/"

def build_headers(token: Optional[str]) -> Dict[str, str]:
    h = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "git-gud-stats-app",
    }
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h

def extract_token(credentials: Optional[HTTPAuthorizationCredentials]) -> Optional[str]:
    """
    Accept:
      Authorization: Bearer <token>
      Authorization: token <token>
    Fallback to env GITHUB_TOKEN if header missing.
    """
    if credentials and credentials.scheme:
        raw = credentials.credentials.strip()
        return raw
    env_token = os.getenv("GITHUB_TOKEN")
    return env_token.strip() if env_token else None

@app.get("/")
def root():
    return {"message": "GitHub User Info API"}

@app.get("/user/{username}")
async def get_github_user(
    username: str,
    credentials: Optional[HTTPAuthorizationCredentials] = Security(bearer_scheme),
):
    token = extract_token(credentials)
    headers = build_headers(token)
    async with httpx.AsyncClient(timeout=15) as client:
        resp = await client.get(f"{GITHUB_API_URL}{username}", headers=headers)
        if resp.status_code == 404:
            raise HTTPException(status_code=404, detail="User not found")
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail=resp.text)
        return resp.json()

# shows Authorize button
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    schema = get_openapi(
        title="GitHub Stats API",
        version="0.1.0",
        description="Fetch GitHub user data with optional Bearer token (PAT).",
        routes=app.routes,
    )
    schema.setdefault("components", {}).setdefault("securitySchemes", {})
    schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = schema
    return schema

app.openapi = custom_openapi

# Debug endpoint to verify if swagger is sending Authorization header
@app.get("/debug/token")
def debug_token(credentials: Optional[HTTPAuthorizationCredentials] = Security(bearer_scheme)):
    """Diagnose how token is (or isn't) being received.

    Priority order:
    1. Authorization header via Swagger Authorize (HTTPBearer)
    2. GITHUB_TOKEN environment variable (.env loaded)
    """
    header_present = bool(credentials)
    env_token = os.getenv("GITHUB_TOKEN")
    env_present = bool(env_token)
    data = {
        "header_received": header_present,
        "env_present": env_present,
    }
    if header_present:
        token = credentials.credentials or ""
        data.update({
            "scheme": credentials.scheme,
            "header_token_length": len(token),
            "header_preview_start": token[:4],
        })
    if env_present:
        data.update({
            "env_token_length": len(env_token),
            "env_preview_start": env_token[:4],
        })
    data["effective_source"] = "header" if header_present else ("env" if env_present else None)
    data["received"] = header_present or env_present
    return data