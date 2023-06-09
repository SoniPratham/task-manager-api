# task-manager-api


# Flask Task Manager

This is a simple RESTful API for managing tasks using Python and Flask.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/flask-task-manager.git
   ```

2. Navigate to the project directory:
   ```
   cd flask-task-manager
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create the database:
   ```
   flask db create
   ```

5. Run the Flask application:
   ```
   flask run
   ```

   The API will be available at `http://localhost:5000`.

## Endpoints

### Create a new task

- **URL:** `/tasks`
- **Method:** POST
- **Request Body:**
  ```json
  {
    "title": "Task Title",
    "description": "Task description",
    "due_date": "2023-06-30",
    "status": "Incomplete"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "title": "Task Title",
    "description": "Task description",
    "due_date": "2023-06-30",
    "status": "Incomplete"
  }
  ```

### Retrieve a single task by its ID

- **URL:** `/tasks/<task_id>`
- **Method:** GET
- **Response:**
  ```json
  {
    "id": 1,
    "title": "Task Title",
    "description": "Task description",
    "due_date": "2023-06-30",
    "status": "Incomplete"
  }
  ```

### Update an existing task

- **URL:** `/tasks/<task_id>`
- **Method:** PUT
- **Request Body:** (Include only the fields to be updated)
  ```json
  {
    "title": "Updated Task Title",
    "status": "Completed"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "title": "Updated Task Title",
    "description": "Task description",
    "due_date": "2023-06-30",
    "status": "Completed"
  }
  ```

### Delete a task

- **URL:** `/tasks/<task_id>`
- **Method:** DELETE
- **Response:**
  ```json
  {
    "message": "Task deleted successfully"
  }
  ```

### List all tasks with pagination

- **URL:** `/tasks`
- **Method:** GET
- **Query Parameters:**
  - `page` (optional): Page number for pagination (default: 1)
  - `size` (optional): Number of tasks per page (default: 10)
- **Response:**
  ```json
  {
    "tasks": [
      {
        "id": 1,
        "title": "Task Title",
        "description": "Task description",
        "due_date": "2023-06-30",
        "status": "Incomplete"
      },
      ...
    ],
    "total_tasks": 15,
    "current_page": 1,
    "total_pages": 2
  }
  ```

## Error Handling

In case of any errors, the API will return a JSON response with an appropriate error message and status code.

- If a requested task is not found, the API will respond with:
  ```json
  {
    "error": "Task not found"
  }
  ```
## Technologies Used
- Python
- Flask
- SQLite
- SQLAlchemy

