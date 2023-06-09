from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    due_date = db.Column(db.String)
    status = db.Column(db.String(20), default='Incomplete')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'due_date': str(self.due_date),
            'status': self.status
        }


@app.route('/tasks', methods=['POST'])
def create_task():
    """
    Create a new task.
    """
    data = request.json
    task = Task(title=data['title'],
                description=data.get('description'),
                due_date=data.get('due_date'),
                status=data.get('status', 'Incomplete'))
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """
    Retrieve a single task by its ID.
    """
    task = Task.query.get(task_id)
    if task:
        return jsonify(task.to_dict()), 200
    return jsonify({'error': 'Task not found'}), 404


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    Update an existing task.
    """
    task = Task.query.get(task_id)
    if task:
        data = request.json
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.due_date = data.get('due_date', task.due_date)
        task.status = data.get('status', task.status)
        db.session.commit()
        return jsonify(task.to_dict()), 200
    return jsonify({'error': 'Task not found'}), 404


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Delete a task.
    """
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully'}), 200
    return jsonify({'error': 'Task not found'}), 404


@app.route('/tasks', methods=['GET'])
def list_tasks():
    """
    List all tasks with pagination.
    """
    page = request.args.get('page', default=1, type=int)
    size = request.args.get('size', default=10, type=int)

    tasks = Task.query.paginate(page=page, per_page=size)

    task_list = [task.to_dict() for task in tasks.items]

    return jsonify({
        'tasks': task_list,
        'total_tasks': tasks.total,
        'current_page': tasks.page,
        'total_pages': tasks.pages
    }), 200


if __name__ == '__main__':
    # Task.__table__.drop(db.engine, checkfirst=True)
    with app.app_context():
        # Perform database operations here
        print("-------------@@")
        db.create_all()
        db.session.commit()
        print("----------###")  
    
    # Create the database and tables
    # print(db.create_all())
    # Run the Flask application
    app.run()
