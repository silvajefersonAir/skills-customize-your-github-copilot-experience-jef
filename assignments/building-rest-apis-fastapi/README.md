# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API with FastAPI, define routes, validate input data, and return JSON responses in a clean and professional way.

## 📝 Tasks

### 🛠️ Create the Base API

#### Descrição
Create a FastAPI application that exposes endpoints for managing a simple list of tasks.

#### Requisitos
O programa completo deve:

- Create a FastAPI app with a title and a basic description.
- Define a route to list all tasks at `GET /tasks`.
- Define a route to create a new task at `POST /tasks`.
- Use a Pydantic model to validate task data.
- Return data in JSON format.

### 🛠️ Add Details and Validation

#### Descrição
Improve the API so each task includes useful information and validation rules.

#### Requisitos
O programa completo deve:

- Include fields such as `id`, `title`, and `completed`.
- Validate that `title` is a non-empty string.
- Prevent invalid payloads from being accepted.
- Return a `201 Created` response when a task is added.

### 🛠️ Build a Complete CRUD Flow

#### Descrição
Extend the API so it supports retrieving, updating, and deleting tasks by id.

#### Requisitos
O programa completo deve:

- Add `GET /tasks/{task_id}` to retrieve a single task.
- Add `PUT` or `PATCH` to update an existing task.
- Add `DELETE /tasks/{task_id}` to remove a task.
- Return `404 Not Found` when a task does not exist.
- Keep the API responses consistent and predictable.

### 🛠️ Test the API

#### Descrição
Run the FastAPI app and verify the endpoints using a browser or an HTTP client.

#### Requisitos
O programa completo deve:

- Start the app successfully with Uvicorn.
- Test at least the `GET /tasks` and `POST /tasks` routes.
- Confirm that the API returns valid JSON payloads.
- Document one example request and one example response.
