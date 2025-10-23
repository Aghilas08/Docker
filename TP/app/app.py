from flask import Flask, jsonify, request
import os, json

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "tasks.json")

# Charger les tâches
def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Sauvegarder les tâches
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(load_tasks())

@app.route("/tasks", methods=["POST"])
def add_task():
    tasks = load_tasks()
    new_task = request.json
    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify(new_task), 201

if __name__ == "__main__":
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    app.run(host="0.0.0.0", port=5000)
