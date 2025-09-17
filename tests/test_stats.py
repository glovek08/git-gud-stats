import pytest
import respx
import os
from unittest.mock import patch
from httpx import Response
from fastapi.testclient import TestClient
from starlette import status
from fastapi.security.http import HTTPAuthorizationCredentials

from app.main import app
from app.routers.stats import GITHUB_API_URL
from app.routers.stats import GITHUB_GRAPHQL_URL


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
    respx.get(mock_url).mock(return_value=Response(status.HTTP_200_OK, json={"login": "testuser", "public_repos": 10}))

    response = client.get("/stats/user/testuser", headers=auth_header)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["login"] == "testuser"
    assert "public_repos" in response.json()

@respx.mock
def test_get_github_user_not_found(auth_header):
    mock_url = f"{GITHUB_API_URL}nonexistentuser"
    respx.get(mock_url).mock(return_value=Response(status.HTTP_404_NOT_FOUND, json={"message": "Not Found"}))

    response = client.get("/stats/user/nonexistentuser", headers=auth_header)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "User not found"

@respx.mock
def test_get_github_user_api_error(auth_header):
    mock_url = f"{GITHUB_API_URL}erroruser"
    respx.get(mock_url).mock(return_value=Response(status.HTTP_500_INTERNAL_SERVER_ERROR, text="Internal Server Error"))

    response = client.get("/stats/user/erroruser", headers=auth_header)

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert response.json()["detail"] == "Internal Server Error"



"""
-------------------------------- ENDPOINT GRAPHQL --------------------------------
"""
@respx.mock
def test_github_graphql_user_success(auth_header): 
    username = "testuser"

    query = """
        query($login: String!) {
          user(login: $login) {
            name
            repositories(first: 50, orderBy: {field: STARGAZERS, direction: DESC}, isFork: false, isArchived:false, privacy: PUBLIC) {
              nodes {
                name
                diskUsage
                languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
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
    body_for_github_api = {"query": query, "variables": {"login": username}}

    respx.post(GITHUB_GRAPHQL_URL, json=body_for_github_api).mock(
        return_value=Response(status.HTTP_200_OK, json={
            "data": {
                "user": {
                    "name": "testuser",
                    "repositories": {
                        "nodes": []
                    }
                }
            }
        })
    )

    response = client.get(f"/stats/graphql-user/{username}", headers=auth_header) 
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == username
    assert isinstance(response.json()["stack"], list)

@respx.mock
def test_github_graphql_user_not_found(auth_header): 
    username = "userNotFound"

    query = """
        query($login: String!) {
          user(login: $login) {
            name
            repositories(first: 50, orderBy: {field: STARGAZERS, direction: DESC}, isFork: false, isArchived:false, privacy: PUBLIC) {
              nodes {
                name
                diskUsage
                languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
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
    body_for_github_api = {"query": query, "variables": {"login": username}}

    respx.post(GITHUB_GRAPHQL_URL, json=body_for_github_api).mock(
        return_value=Response(status.HTTP_200_OK, json={
            "data": {
                "user": None
            }
        })
    )

    response = client.get(f"/stats/graphql-user/{username}", headers=auth_header) 
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "user not found"

@respx.mock
def test_github_graphql_data_error(auth_header): 
    username = "testuser"
    
    query = """
        query($login: String!) {
          user(login: $login) {
            name
            repositories(first: 50, orderBy: {field: STARGAZERS, direction: DESC}, isFork: false, isArchived:false, privacy: PUBLIC) {
              nodes {
                name
                diskUsage
                languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
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
    body_for_github_api = {"query": query, "variables": {"login": username}}
    
    respx.post(GITHUB_GRAPHQL_URL, json=body_for_github_api).mock(
        return_value=Response(status.HTTP_200_OK, json={
            "data": None,
            "errors": [
                {
                    "message": "Some error message from GitHub",
                    "type": "OTHER_ERROR"
                }
            ]
        })
    )

    response = client.get(f"/stats/graphql-user/{username}", headers=auth_header) 
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == [
        {
            "message": "Some error message from GitHub",
            "type": "OTHER_ERROR"
        }
    ]

@respx.mock
def test_github_graphql_without_token(auth_header): 
    username = "testuser"
    
    query = """
        query($login: String!) {
          user(login: $login) {
            name
            repositories(first: 50, orderBy: {field: STARGAZERS, direction: DESC}, isFork: false, isArchived:false, privacy: PUBLIC) {
              nodes {
                name
                diskUsage
                languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
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
    body_for_github_api = {"query": query, "variables": {"login": username}}
    
    respx.post(GITHUB_GRAPHQL_URL, json=body_for_github_api).mock(
        return_value=Response(status.HTTP_200_OK, json={
            "data": {
                "user": {
                    "name": "testuser",
                    "repositories": {
                        "nodes": []
                    }
                }
            }
        })
    )

    response = client.get(f"/stats/graphql-user/{username}") 
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Github token is required'}


"""
-------------------------------- DEBUG/TOKEN --------------------------------
"""
@patch.dict(os.environ, {}, clear=True)
def test_debug_token_no_token():
    response = client.get("stats/debug/token")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["header_received"] == False
    assert data["env_present"] == False
    assert data["effective_source"] == None
    assert data["received"] == False

@patch.dict(os.environ, {}, clear=True)
def test_debug_token_on_header(auth_header):
    response = client.get("stats/debug/token", headers=auth_header)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["header_received"] == True
    assert data["env_present"] == False
    assert data["effective_source"] == "header"
    assert data["received"] == True

@patch.dict(os.environ, {"GITHUB_TOKEN":"fake-token"}, clear=True)
def test_debug_token_on_env():
    response = client.get("stats/debug/token")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["header_received"] == False
    assert data["env_present"] == True
    assert data["effective_source"] == "env"
    assert data["received"] == True
    assert "env_token_length" in data
    assert "env_preview_start" in data

@patch.dict(os.environ, {"GITHUB_TOKEN":"fake-token"}, clear=True)
def test_debug_token_all_opc(auth_header):
    response = client.get("stats/debug/token", headers=auth_header)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["header_received"] == True
    assert data["env_present"] == True
    assert data["effective_source"] == "header"
    assert data["received"] == True

