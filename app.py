from flask import Flask, request, jsonify

app = Flask(__name__)

# in memory database
lists = []
task_id = 1

# create task - POST /tasks
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id
    data = request.get_json()
    task = {
        'id': task_id,
        'title': data['title'],
        'description': data.get('description', ''),
        'done': False
    }
    lists.append(task)
    task_id += 1
    return jsonify(task), 201


if __name__ == "__main__":
    app.run(debug=True)