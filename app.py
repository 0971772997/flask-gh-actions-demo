from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello CI/CD'

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

@app.route('/sum/<int:a>/<int:b>')
def sum_route(a, b):
    return str(a + b)