import pytest
from flask import json
from api.app import app, get_db_connection

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Hello!, dupa" in rv.data

def test_get_tasks(client, monkeypatch):
    def mock_get_db_connection():
        class MockCursor:
            def execute(self, query):
                pass
            def fetchall(self):
                return [{'id': 1, 'title': 'Test Task', 'description': 'Test Description', 'priority': 'high', 'due_date': '2023-10-10', 'created_at': '2023-10-01'}]
            def close(self):
                pass
        class MockConnection:
            def cursor(self, dictionary=True):
                return MockCursor()
            def close(self):
                pass
            def commit(self):
                pass
        return MockConnection()
    
    monkeypatch.setattr('api.app.get_db_connection', mock_get_db_connection)
    rv = client.get('/v1/tasks')
    assert rv.status_code == 200
    data = json.loads(rv.data)
    assert len(data) == 1
    assert data[0]['title'] == 'Test Task'

def test_get_task(client, monkeypatch):
    def mock_get_db_connection():
        class MockCursor:
            def execute(self, query, params):
                pass
            def fetchone(self):
                return {'id': 1, 'title': 'Test Task', 'description': 'Test Description', 'priority': 'high', 'due_date': '2023-10-10', 'created_at': '2023-10-01'}
            def close(self):
                pass
        class MockConnection:
            def cursor(self, dictionary=True):
                return MockCursor()
            def close(self):
                pass
            def commit(self):
                pass
        return MockConnection()
    
    monkeypatch.setattr('api.app.get_db_connection', mock_get_db_connection)
    rv = client.get('/v1/tasks/1')
    assert rv.status_code == 200
    data = json.loads(rv.data)
    assert data['title'] == 'Test Task'

def test_create_task(client, monkeypatch):
    def mock_get_db_connection():
        class MockCursor:
            def execute(self, query, params):
                pass
            @property
            def lastrowid(self):
                return 1
            def close(self):
                pass
        class MockConnection:
            def cursor(self):
                return MockCursor()
            def close(self):
                pass
            def commit(self):
                pass
        return MockConnection()
    
    monkeypatch.setattr('api.app.get_db_connection', mock_get_db_connection)
    rv = client.post('/v1/tasks', json={
        'title': 'New Task',
        'description': 'New Description',
        'priority': 'medium'
    })
    assert rv.status_code == 201
    data = json.loads(rv.data)
    assert data['title'] == 'New Task'

def test_update_task(client, monkeypatch):
    def mock_get_db_connection():
        class MockCursor:
            def execute(self, query, params):
                pass
            def fetchone(self):
                return {'id': 1, 'title': 'Test Task', 'description': 'Test Description', 'priority': 'high', 'due_date': '2023-10-10', 'created_at': '2023-10-01'}
            def close(self):
                pass
        class MockConnection:
            def cursor(self):
                return MockCursor()
            def close(self):
                pass
            def commit(self):
                pass
        return MockConnection()
    
    monkeypatch.setattr('api.app.get_db_connection', mock_get_db_connection)
    rv = client.put('/v1/tasks/1', json={
        'title': 'Updated Task',
        'description': 'Updated Description',
        'priority': 'low'
    })
    assert rv.status_code == 200
    data = json.loads(rv.data)
    assert data['message'] == 'Task updated successfully'

def test_delete_task(client, monkeypatch):
    def mock_get_db_connection():
        class MockCursor:
            def execute(self, query, params):
                pass
            def fetchone(self):
                return {'id': 1, 'title': 'Test Task', 'description': 'Test Description', 'priority': 'high', 'due_date': '2023-10-10', 'created_at': '2023-10-01'}
            def close(self):
                pass
        class MockConnection:
            def cursor(self):
                return MockCursor()
            def close(self):
                pass
            def commit(self):
                pass
        return MockConnection()
    
    monkeypatch.setattr('api.app.get_db_connection', mock_get_db_connection)
    rv = client.delete('/v1/tasks/1')
    assert rv.status_code == 200
    data = json.loads(rv.data)
    assert data['message'] == 'Task deleted successfully'
