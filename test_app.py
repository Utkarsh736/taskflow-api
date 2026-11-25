import pytest
from app import app, db

@pytest.fixture
def client():
    # Configure the app for testing
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' # Use an in-memory DB for tests!
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_register_and_login(client):
    # 1. Test Registration
    resp = client.post('/register', json={'username': 'testuser', 'password': 'pass'})
    assert resp.status_code == 201
    assert resp.json['msg'] == 'User created successfully'

    # 2. Test Login and get a token
    resp = client.post('/login', json={'username': 'testuser', 'password': 'pass'})
    assert resp.status_code == 200
    assert 'access_token' in resp.json
    token = resp.json['access_token']

    # 3. Test a protected route with the token
    headers = {'Authorization': f'Bearer {token}'}
    resp = client.post('/tasks', json={'title': 'Test Task'}, headers=headers)
    assert resp.status_code == 201
    assert resp.json['msg'] == 'Task created'

def test_unauthorized_access(client):
    # Try to access a protected route without a token
    resp = client.get('/tasks')
    assert resp.status_code == 401
