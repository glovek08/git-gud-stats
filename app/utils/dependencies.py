import os
from typing import Optional, Dict
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

bearer_scheme = HTTPBearer(auto_error=False)


def build_headers(token: Optional[str]) -> Dict[str, str]:
    h = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "git-gud-stats-app",
    }
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def extract_token(
    credentials: Optional[HTTPAuthorizationCredentials],
) -> Optional[str]:
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
