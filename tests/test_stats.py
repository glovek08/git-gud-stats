import pytest
import respx
from httpx import Response
from fastapi.testclient import TestClient

from app.main import app
from app.routers.stats import GITHUB_API_URL

client = TestClient(app)

"""
-------------------------------- FIRST ENDPOINT --------------------------------
"""
@pytest.fixture
def auth_header():
    return {"Authorization": "Bearer fake_token"}

@respx.mock
def test_get_github_user_seccess(auth_header):
    mock_url = f"{GITHUB_API_URL}testuser"
    respx.get(mock_url).mock(return_value=Response(200, json={"login": "testuser", "public_repos": 10}))

    response = client.get("/stats/user/testuser", headers=auth_header)

    assert response.status_code == 200
    assert response.json()["login"] == "testuser"
    assert "public_repos" in response.json()

@respx.mock
def test_get_github_user_not_found(auth_header):
    mock_url = f"{GITHUB_API_URL}nonexistentuser"
    respx.get(mock_url).mock(return_value=Response(404, json={"message": "Not Found"}))

    response = client.get("/stats/user/nonexistentuser", headers=auth_header)

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

@respx.mock
def test_get_github_user_api_error(auth_header):
    mock_url = f"{GITHUB_API_URL}erroruser"
    respx.get(mock_url).mock(return_value=Response(500, text="Internal Server Error"))

    response = client.get("/stats/user/erroruser", headers=auth_header)

    assert response.status_code == 500
    assert response.json()["detail"] == "Internal Server Error"


"""
-------------------------------- ENDPOINT GRAPHQL --------------------------------
"""