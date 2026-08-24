import requests
from models import db, Todo

EXTERNAL_API_URL = 'https://jsonplaceholder.typicode.com/todos'

def todos_from_api():
    try:
        response = requests.get(EXTERNAL_API_URL, timeout=5)

        response.raise_for_status()

        return response.json()
        pass

    except requests.exceptions.Timeout:
        print("Error: External API time out")
        return []

    except requests.exceptions.ConnectionError:
        print("Error: unable to connect to Todo external API")
        return []
    
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")

        return []
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching todos: {e}")
        return []

def display_todos_api():
    print('Fetching todos from the external API........')

    todosData = todos_from_api()

    if not todosData:
        print("No todos data has been fetched")

        return 

    count = 0
    for item in todosData:
        existing = Todo.query.filter_by(id=item.get('id')).first()

        if existing:
            continue

        todo = Todo(
            id = item.get('id'),
            title = item.get('title', 'untitled'),
            description = '',
            completed = item.get('completed', False)
        )

        db.session.add(todo)
        count = count + 1

        db.session.commit()
        print(f"Success adding {count} todos into the db from external api")

        