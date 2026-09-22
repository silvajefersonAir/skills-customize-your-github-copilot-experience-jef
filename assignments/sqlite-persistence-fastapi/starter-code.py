import sqlite3
from typing import Any

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


DATABASE_PATH = "tasks.db"
app = FastAPI(title="Persistent Task API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1)
    completed: bool | None = None


class Task(TaskCreate):
    id: int


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database() -> None:
    connection = get_connection()
    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        connection.commit()
    finally:
        connection.close()


@app.on_event("startup")
def startup() -> None:
    initialize_database()


def row_to_task(row: sqlite3.Row) -> dict[str, Any]:
    return {
        "id": row["id"],
        "title": row["title"],
        "completed": bool(row["completed"]),
    }


@app.get("/tasks", response_model=list[Task])
def get_tasks() -> list[dict[str, Any]]:
    raise NotImplementedError("Implement the SELECT query")


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate) -> dict[str, Any]:
    raise NotImplementedError("Implement the INSERT query")


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> dict[str, Any]:
    raise NotImplementedError("Implement the SELECT query for one task")


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskUpdate) -> dict[str, Any]:
    raise NotImplementedError("Implement the UPDATE query")


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> None:
    raise NotImplementedError("Implement the DELETE query")