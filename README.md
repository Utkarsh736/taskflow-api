# TaskFlow API

A robust RESTful API for task management, designed to serve as the backend for mobile applications. Built with Python and Flask, this API features secure JWT authentication and a relational database.

## 🚀 Tech Stack
*   **Framework:** Flask
*   **Database:** SQLite (via SQLAlchemy ORM)
*   **Authentication:** JWT (JSON Web Tokens)
*   **Testing:** Pytest
*   **Package Manager:** uv

## 🛠️ Features
*   **User Authentication:** Secure registration and login using hashed passwords.
*   **JWT Protection:** All task-related endpoints are protected and scoped to the authenticated user.
*   **CRUD Operations:** Create, read, update, and delete tasks.
*   **Automated Testing:** Comprehensive integration tests for auth and task flows.

## 🏁 Getting Started

### Prerequisites
Make sure you have [uv](https://github.com/astral-sh/uv) installed.

### Installation
Clone the repository and install the dependencies:
```bash
git clone <your-repo-url>
cd taskflow-api
uv sync
```
### Running the App
Start the development server:

```bash
uv run app.py
```
The API will be available at `http://127.0.0.1:5000`.

### Running Tests
Execute the test suite to ensure everything is working:

```bash
uv run pytest
```

## 📡 API Endpoints

| Method   | Endpoint      | Description                     | Auth Required |
| -------- | ------------- | ------------------------------- | ------------- |
| `POST`   | `/register`   | Create a new user account       | No            |
| `POST`   | `/login`      | Authenticate and receive a JWT  | No            |
| `GET`    | `/tasks`      | Retrieve all tasks for the user | Yes           |
| `POST`   | `/tasks`      | Create a new task               | Yes           |
| `PUT`    | `/tasks/<id>` | Update an existing task         | Yes           |
| `DELETE` | `/tasks/<id>` | Delete a task                   | Yes           |
