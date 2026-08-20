from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, TodoList API + Basic Auth"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=True)

    