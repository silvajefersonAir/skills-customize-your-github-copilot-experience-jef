# 📘 Assignment: SQLite Persistence with FastAPI

## 🎯 Objective

Extend a FastAPI task API so that its data is stored in a SQLite database instead of being kept only in memory. You will practice database initialization, SQL queries, CRUD operations, validation, and persistence across server restarts.

## 📝 Tasks

### 🛠️ Create the SQLite Database

#### Descrição
Complete the database setup in the starter code. The application should create a `tasks` table automatically when it starts and use a separate SQLite connection for each operation.

#### Requisitos
O programa concluído deve:

- Create a local database file named `tasks.db`.
- Create the `tasks` table if it does not already exist.
- Store an integer `id`, a required `title`, and a boolean-compatible `completed` value.
- Close each database connection after the operation finishes.

### 🛠️ Store and List Tasks

#### Descrição
Replace the in-memory list used by the API with SQLite queries for creating and listing tasks.

#### Requisitos
O programa concluído deve:

- Insert new tasks with `POST /tasks`.
- Return the created task with its generated database id.
- Return all saved tasks with `GET /tasks`.
- Convert SQLite values into the same JSON shape used by the API models.

### 🛠️ Complete the Persistent CRUD Flow

#### Descrição
Implement the remaining task endpoints using parameterized SQL statements. The API must behave consistently whether a task was created during the current run or before the server was restarted.

#### Requisitos
O programa concluído deve:

- Retrieve one task with `GET /tasks/{task_id}`.
- Update a task with `PATCH /tasks/{task_id}`.
- Delete a task with `DELETE /tasks/{task_id}`.
- Return `404 Not Found` when the requested task does not exist.
- Avoid building SQL statements by concatenating user input.

### 🛠️ Validate and Test Persistence

#### Descrição
Add input validation and verify the API with FastAPI's interactive documentation or an HTTP client. Then restart the server and confirm that existing records remain available.

#### Requisitos
O programa concluído deve:

- Reject an empty task title with a validation error.
- Accept only valid boolean values for the `completed` field.
- Return `201 Created` when a task is created.
- Test at least one successful request and one `404` request.
- Document an example request, response, and persistence check in your submission.
