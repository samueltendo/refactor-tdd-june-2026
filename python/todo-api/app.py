from flask import Flask
from flask import request, jsonify
import uuid

app = Flask(__name__)


@app.route("/health")
def health():
    return "", 200


def validate_title(title):
    if not isinstance(title, str):
        return False
    return len(title.strip()) > 0


todos_store = {}

@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    title = data.get("title")

    if not validate_title(title):
        return jsonify({"error": "invalid title"}), 400

    todo_id = str(uuid.uuid4())
    todos_store[todo_id] = {"id": todo_id, "title": title, "completed": False}
    return jsonify(todos_store[todo_id]), 201

@app.route("/todos", methods=["GET"])
def list_todos():
    return jsonify(list(todos_store.values())), 200

@app.route("/todos/<todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = todos_store.get(todo_id)
    if todo is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(todo), 200

@app.route("/todos/<todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    if todo_id not in todos_store:
        return jsonify({"error": "not found"}), 404
    del todos_store[todo_id]
    return "", 204


@app.route("/todos/<todo_id>", methods=["PATCH"])
def update_todo(todo_id):
    todo = todos_store.get(todo_id)
    if todo is None:
        return jsonify({"error": "not found"}), 404

    data = request.get_json()

    if "title" in data:
        if not validate_title(data["title"]):
            return jsonify({"error": "invalid title"}), 400
        todo["title"] = data["title"]

    if "completed" in data:
        todo["completed"] = bool(data["completed"])

    return jsonify(todo), 200
