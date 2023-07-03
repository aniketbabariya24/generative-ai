from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello, World!'

@app.route('/greet/<username>')
def greet(username):
    return f'Hello, {username}!'

@app.route('/farewell/<username>')
def fare(username):
    return f'Goodbye, {username}!'


if __name__ == '__main__':
    app.run()