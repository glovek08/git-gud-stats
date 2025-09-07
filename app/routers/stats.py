from fastapi import APIRouter, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials
from typing import Optional, Dict, Any
import httpx

from ..dependencies import bearer_scheme, build_headers, extract_token

router = APIRouter(
    prefix="/stats",
    tags=["stats"],
)

GITHUB_API_URL = "https://api.github.com/users/"
GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"

@router.get("/user/{username}")
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

@router.get("/graphql-user/{username}")
async def get_graphql_user_data(username: str, credentials: Optional[HTTPAuthorizationCredentials] = Security(bearer_scheme)):
    token = extract_token(credentials)
    if not token:
        raise HTTPException(status_code=401, detail="Github token is required")

    headers = build_headers(token)
    headers['Content-type'] = 'application/json'

    query = """
        query($login: String!) {
          user(login: $login) {
            name
            repositories(first: 5, orderBy: {field: PUSHED_AT, direction: DESC}) {
              nodes {
                name
                languages(first: 5, orderBy: {field: SIZE, direction: DESC}) {
                  edges {
                    size
                    node {
                      name
                    }
                  }
                }
              }
            }
          }
        }
    """

    body = {
        "query": query,
        "variables": {
            "login": username
        }
    }

    async with httpx.AsyncClient(timeout=15) as client:
        resp = await client.post(GITHUB_GRAPHQL_URL, headers=headers, json=body)

        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail=resp.text)
        
        data = resp.json()

        if 'errors' in data:
            raise HTTPException(status_code=400, detail=data['errors'])

        if data['data']['user'] is None:
            raise HTTPException(status_code=400, detail="user not found")

        return data['data']['user']

@router.get("/debug/token") # tags=["debug"] use it to sort swagger ui endpoints
def debug_token(credentials: Optional[HTTPAuthorizationCredentials] = Security(bearer_scheme)) -> Dict[str, Any]:
    """Diagnose how token is (or isn't) being received."""
    import os
    header_present = bool(credentials)
    env_token = os.getenv("GITHUB_TOKEN")
    env_present = bool(env_token)
    data: Dict[str, Any] = {
        "header_received": header_present,
        "env_present": env_present,
    }
    if header_present:
        token = credentials.credentials or ""
        data["scheme"] = credentials.scheme
        data["header_token_length"] = len(token)
        data["header_preview_start"] = token[:4]
    if env_present:
        data.update({
            "env_token_length": len(env_token),
            "env_preview_start": env_token[:4],
        })
    data["effective_source"] = "header" if header_present else ("env" if env_present else None)
    data["received"] = header_present or env_present
    return data