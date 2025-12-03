from flask import Flask

app = Flask(__name__)

@app.route('/') # www.domain.com/
def index():
    return "<h1>Todo Index Page</h1>"