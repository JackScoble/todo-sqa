from flask import Flask

app = Flask(__name__)

@app.route('/') # www.domain.com/
def index():
    return "<h1>Todo Index Page</h1>"

@app.route('/tasks') # www.domain.com/tasks
def all_tasks():
    return "<h1>All Tasks Page</h1>"