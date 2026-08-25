import pytest
from app import app, db
from requests.auth import HTTPBasicAuth




@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:

        with app.app_context():

            db.create_all()
            yield client
            db.drop_all()

    pass

def auth_headers():
    import base64

    # auth = HTTPBasicAuth('admin', 'secret')
    credentials = 'admin:secret'

    # headers = {}      # auth headers for the admin test
    # auth(headers)

    encodedSecret = base64.b64encode(credentials.encode()).decode()

    return {
        'Authorization': f"Basic {encodedSecret}"
    }

def test_get_todos_unauthorized(client):    # ==== Testing GET /api/todos  ===
    
    response = client.get('/api/todos')   # getting todos without authentication
    assert response.status_code == 401

def test_get_todos_authorized(client):      # Getting todos with authentication
    
    response = client.get('/api/todos', headers = auth_headers())

    assert response.status_code == 200

    assert isinstance(response.json, list)


def test_create_todo_success(client):   # testing POST api/todos with corect data
    
    data = {
        'title': 'Testing Todo',
        'description': 'This is a test todo',
        'completed': False
    }

    response = client.post(
        '/api/todos', 
        json = data, 
        headers = auth_headers()
    )

    assert response.status_code == 201
    assert response.json['title'] == 'Testing Todo'

 