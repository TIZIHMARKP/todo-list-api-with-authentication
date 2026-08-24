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


@todo_bp.route('/todos/<int:todo_id>', methods = ['GET'])
def get_todo(todo_id):                        # Getting a todo by id
    todo = get_todo_or_404(todo_id)

    if todo is None:
        return jsonify({
            "error": f"Not found todo with id {todo_id}"
        }), 404

    return jsonify(todo.to_dict()), 200


@todo_bp.route('/todos', methods=['POST'])
def create_todo():                          # creating a new todo

    if not request.is_json:   # ensuring that request is json
        return jsonify({
            "error": "Request should be json"
        }), 400

    try: 
        
        data = request.get_json()
    except Exception as e:
        return jsonify({
            "error": f"You have invalid json: {str(e)}"
        }), 400

    title = data.get('title')    # validating title
    if not title:
        return jsonify({"error": "Title must be present"}), 400

    description = data.get('description', '')  # optional
    completed = data.get('completed', False)

    new_todo = Todo(
        title=title,

        description=description,

        completed=completed
    )
    
    db.session.add(new_todo)
    db.session.commit()
    
    return jsonify(new_todo.to_dict()), 201


@todo_bp.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):                            # Updating a todo by ID

    todo = get_todo_or_404(todo_id)
    if todo is None:
        return jsonify({
            "error": f"Not found todo with id {todo_id}"
        }), 404
    
    if not request.is_json:  
        return jsonify({
            "error": "Request should be json"
        }), 400
    
    data = request.get_json() 

    if 'title' in data:
        todo.title = data['title']

    if 'description' in data:
        todo.description = data['description']

    if 'completed' in data:
        todo.completed = data['completed']
    
    db.session.commit()
    
    return jsonify(todo.to_dict()), 200


@todo_bp.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):                              # Deleting a todo   

    todo = get_todo_or_404(todo_id)

    if todo is None:
        return jsonify({
            "error": f"Not found todo with id {todo_id}"
        }), 404
    
    db.session.delete(todo)
    db.session.commit()
    
    return jsonify({
        "message": f"Success deleting todo {todo_id}"
    }), 200


@todo_bp.route('/todos/completed', methods=['GET'])
def get_completed_todos():                             # Getting completed todos

    todos = Todo.query.filter_by(
        completed=True
    ).all()

    result = []
    for todo in todos:
        result.append(todo.to_dict())

    return jsonify(result), 200



