from flask import Flask

app = Flask(__name__)

@app.route('/') # www.domain.com/
def index():
    return "<h1>Todo Index Page</h1>"

@app.route('/tasks') # www.domain.com/tasks
def all_tasks():
    return "<h1>All Tasks Page</h1>"

@app.route('/task/<int:task_id>') # www.domain.com/task/1
def task_detail(task_id):
    return f"<h1>Task Detail Page for Task ID: {task_id}</h1>"