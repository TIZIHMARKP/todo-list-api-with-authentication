from flask import Flask
from config import Config
from models import db, Todo
from routes import todo_bp
from services.todo_services import display_todos_api
from utils.logger import log_request


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)  # db init

app.register_blueprint(todo_bp)   # blueprint reg

@app.before_request
def before_request():

    log_request()  # all incoming request are visible in app.log


with app.app_context():
    db.create_all()
    print("Success creating database tables")

    display_todos_api()    # Adding the external fetch todos into the database

@app.route('/')
def index():
    return {"message": "TodoList API is running on port 8082"}

@app.route('/count-test')
def test_count():
    count = Todo.query.count()
    return {"totalTodos": count}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=True)

    