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


def test_get_todo_returns_existing():
    client = app.test_client()
    create_response = client.post("/todos", json={"title": "Buy milk"})
    todo_id = create_response.get_json()["id"]

    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.get_json()["id"] == todo_id
    
def test_get_todo_not_found_returns_404():
    client = app.test_client()
    response = client.get("/todos/does-not-exist")
    assert response.status_code == 404
    
def test_delete_todo_removes_it():
    client = app.test_client()
    create_response = client.post("/todos", json={"title": "Buy milk"})
    todo_id = create_response.get_json()["id"]

    delete_response = client.delete(f"/todos/{todo_id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/todos/{todo_id}")
    assert get_response.status_code == 404

def test_delete_todo_not_found_returns_404():
    client = app.test_client()
    response = client.delete("/todos/does-not-exist")
    assert response.status_code == 404
    
    
def test_patch_todo_updates_title():
    client = app.test_client()
    create_response = client.post("/todos", json={"title": "Buy milk"})
    todo_id = create_response.get_json()["id"]

    response = client.patch(f"/todos/{todo_id}", json={"title": "Buy oat milk"})
    assert response.status_code == 200
    assert response.get_json()["title"] == "Buy oat milk"

def test_patch_todo_toggles_completed():
    client = app.test_client()
    create_response = client.post("/todos", json={"title": "Buy milk"})
    todo_id = create_response.get_json()["id"]

    response = client.patch(f"/todos/{todo_id}", json={"completed": True})
    assert response.status_code == 200
    assert response.get_json()["completed"] is True

def test_patch_todo_invalid_title_returns_400():
    client = app.test_client()
    create_response = client.post("/todos", json={"title": "Buy milk"})
    todo_id = create_response.get_json()["id"]

    response = client.patch(f"/todos/{todo_id}", json={"title": ""})
    assert response.status_code == 400

def test_patch_todo_not_found_returns_404():
    client = app.test_client()
    response = client.patch("/todos/does-not-exist", json={"title": "x"})
    assert response.status_code == 404
