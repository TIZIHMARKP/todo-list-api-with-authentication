# Todo List API + Basic Authentication

A RESTful Flask API for managing todo items with basic authentication, built as a learning project during my Backend Course at Techcrush to demonstrate API development, authentication, external API integration, and testing

---

## About the Project

This is a simple but complete Todo List API that allows users to create, read, update, and delete todo items. The API uses HTTP Basic Authentication to protect all endpoints and includes features like filtering completed todos, logging requests, and fetching sample data from an external API on startup

This project was built as a learning exercise to understand REST API development with Flask, authentication, logging, and testing

---

## Features

- **CRUD Operations** – Create, read, update, and delete todos
- **Basic Authentication** – All endpoints protected with HTTP Basic Auth (admin/secret)
- **External API Integration** – Fetches sample todos from JSONPlaceholder on starting the server
- **Filtering** – Get only completed todos with `/api/todos/completed`
- **Request Logging** – All requests logged to a file (app.log) using `before_request` hook
- **Error Handling** – Proper JSON error responses with appropriate status codes
- **Testing** – Basic test suite for API endpoints

---

## Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy (SQLite database)
- Flask-HTTPAuth (Basic Authentication)
- Requests (External API calls)
- Pytest (Testing)
- SQLite

---

## API Endpoints

- GET `/api/todos`  Get all todos 
- GET  `/api/todos/<id>` Get a specific todo 
- POST  `/api/todos`  Create a new todo
- PUT  `/api/todos/<id>`  Update a todo 
- DELETE  `/api/todos/<id>`  Delete a todo 
- GET  `/api/todos/completed`  Get only completed todos 


## How to Run the Project

1. Clone the repository: ``` https://github.com/TIZIHMARKP/todo-list-api-with-authentication.git ```

2. Create and activate a virtual environment

3. Install dependencies: ```pip install -r requirements.txt ```

4. Set up environment variables (Optional) by creating a .env file

5. Run the application: ```python app.py ```

6. Access the API at ```http://127.0.0.1:8082/api/todos``` and it requires authentication

7. Run the test suite using pytest: ```pytest```


## Authentication

The API uses HTTP Basic Authentication with the following credentials:

| Username | Password |
|--------|----------|
| admin | secret |

All the api routes require authentication. If no user credentials are provided, the API is going to return a 401 Unauthorized response error message

