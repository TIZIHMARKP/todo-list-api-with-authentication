from flask import Flask
from config import Config
from models import db


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)  # db init

with app.app_context():
    db.create_all()
    print("Success creating database tables")

@app.route('/')
def index():
    return {"message": "TodoList API is running on port 8082"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=True)

    