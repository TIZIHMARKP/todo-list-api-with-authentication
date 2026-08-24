from flask import Blueprint, request, jsonify
from models import db, Todo

todo_bp = Blueprint('todo', __name__, url_prefix='/api')

def get_todo_or_404(todo_id):

    todo = Todo.query.get(todo_id)

    if todo is None:
        return None

    return todo

@todo_bp.route('/todos', methods = ['GET'])
def get_todos():                            # Getting all todos
    todos = Todo.query.all()

    result = []
    for todo in todos:
        result.append(todo.to_dict())

    return jsonify(result), 200


@todo_bp.route('/todos/<int:todo_id>', method = ['GET'])
def get_todo(todo_id):                        # Getting a todo by id
    todo = get_todo_or_404(todo_id)

    if todo is None:
        return jsonify({
            "error": f"Not found todo with id {todo_id}"
        }), 404

    return jsonify(todo.to_dict()), 200




