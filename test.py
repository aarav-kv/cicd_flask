import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    return app


@pytest.fixture
def client(app):
    return app.test_client()


# ✅ Test GET /
def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"login": "Hey"}


# ✅ Test POST /login
def test_login(client):
    response = client.post("/login")
    assert response.status_code == 200
    assert response.get_json() == {"login": "failed"}
 