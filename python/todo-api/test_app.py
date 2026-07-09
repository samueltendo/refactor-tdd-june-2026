# to run tests in a given file only
# pytest -v todo-api/test_app.py

from app import app
from app import validate_title

def test_health_returns_200():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200

# Title validation tests
def test_validate_title_rejects_empty_string():
    assert validate_title("") is False

def test_validate_title_rejects_non_string():
    assert validate_title(123) is False

def test_validate_title_rejects_missing():
    assert validate_title(None) is False

def test_validate_title_accepts_nonempty_string():
    assert validate_title("Buy milk") is True

# Creating and retreiving your items
def test_post_todos_valid_returns_201():
    client = app.test_client()
    response = client.post("/todos", json={"title": "Buy milk"})
    assert response.status_code == 201
    body = response.get_json()
    assert body["title"] == "Buy milk"
    assert body["completed"] is False
    assert "id" in body

def test_post_todos_invalid_title_returns_400():
    client = app.test_client()
    response = client.post("/todos", json={"title": ""})
    assert response.status_code == 400

def test_get_todos_returns_list():
    client = app.test_client()
    client.post("/todos", json={"title": "Buy milk"})
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
