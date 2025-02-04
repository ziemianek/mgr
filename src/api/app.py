from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tenacity import retry, wait_fixed, stop_after_attempt
from datetime import datetime, timedelta
import pymysql
from pymysql import Error
import os

app = Flask(__name__)

VERSION = "v1"

# Database connection details from environment variables
DB_CONFIG = {
    'host': os.environ.get('MYSQL_HOST', 'mysql'),  # Use 'mysql' as host from Docker Compose
    'user': os.environ.get('MYSQL_USER', 'testuser'),
    'password': os.environ.get('MYSQL_PASSWORD', 'userpass'),
    'database': os.environ.get('MYSQL_DB', 'taskdb')
}

# SQLAlchemy connection pooling configuration
DATABASE_URI = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 10,
    'max_overflow': 20,
    'pool_timeout': 30,
}

# Initialize the database engine and sessionmaker
engine = create_engine(DATABASE_URI, pool_size=10, max_overflow=20)
Session = sessionmaker(bind=engine)

# Retry logic for database connection
@retry(wait=wait_fixed(2), stop=stop_after_attempt(5))
def get_db_connection():
    """Establish a connection to the MySQL database with retry logic."""
    try:
        # Use PyMySQL to establish connection
        conn = pymysql.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Error: {e}")
        raise e

def calculate_due_date(priority):
    """Calculate due date based on task priority."""
    if priority == 'high':
        return datetime.now() + timedelta(days=1)
    elif priority == 'medium':
        return datetime.now() + timedelta(days=3)
    else:  # low priority
        return datetime.now() + timedelta(days=7)

@app.route('/')
def hello():
    return "Hello!, Flask app with DB connection retry and pooling."

@app.route(f'/{VERSION}/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks."""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    result = cursor.fetchall()
    conn.close()
    return jsonify(result), 200


@app.route(f'/{VERSION}/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a single task."""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    task = cursor.fetchone()
    conn.close()
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task), 200

@app.route(f'/{VERSION}/tasks', methods=['POST'])
def create_task():
    """Create a new task."""
    data = request.json
    title = data.get('title')
    description = data.get('description', '')
    priority = data.get('priority', 'low')

    if not title or priority not in ('high', 'medium', 'low'):
        return jsonify({'error': 'Invalid input'}), 400
    
    due_date = calculate_due_date(priority)

    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500
    
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, priority, due_date, created_at) VALUES (%s, %s, %s, %s, %s)",
        (title, description, priority, due_date, datetime.now())
    )
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()

    return jsonify({'id': task_id, 'title': title, 'priority': priority}), 201

@app.route(f'/{VERSION}/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update an existing task."""
    data = request.json
    title = data.get('title')
    description = data.get('description', '')
    priority = data.get('priority', 'low')

    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({'error': 'Task not found'}), 404

    due_date = calculate_due_date(priority)
    cursor.execute(
        "UPDATE tasks SET title = %s, description = %s, priority = %s, due_date = %s WHERE id = %s",
        (title, description, priority, due_date, task_id)
    )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task updated successfully'}), 200

@app.route(f'/{VERSION}/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task."""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({'error': 'Task not found'}), 404

    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task deleted successfully'}), 200

@app.teardown_appcontext
def shutdown_session(exception=None):
    """Gracefully shutdown the database session on app shutdown."""
    try:
        Session.remove()
    except Exception as e:
        print(f"Error while shutting down session: {e}")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
