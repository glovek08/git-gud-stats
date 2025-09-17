import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Git Gud Stats"}


def test_about_route(client):
    response = client.get("/about")
    assert response.status_code == 404


def test_cors_allowed_origin(client):
    response = client.get("/", headers={"Origin": "http://localhost:5173"})
    assert response.headers["Access-Control-Allow-Origin"] == "http://localhost:5173"


def test_cors_not_allowed_origin(client):
    response = client.get("/", headers={"Origin": "http://evil-site.com"})
    assert "Access-Control-Allow-Origin" not in response.headers


def test_custom_openapi_schema(client):
    response = client.get("/openapi.json")
    schema = response.json()

    assert response.status_code == 200
    assert schema["info"]["title"] == "GitHub Stats API"
    assert schema["info"]["version"] == "0.1.0"
    
    security_schemes = schema["components"]["securitySchemes"]
    assert "HTTPBearer" in security_schemes
    assert security_schemes["HTTPBearer"]["type"] == "http"
    assert security_schemes["HTTPBearer"]["scheme"] == "bearer"

    assert schema["security"] == [{"BearerAuth": []}]