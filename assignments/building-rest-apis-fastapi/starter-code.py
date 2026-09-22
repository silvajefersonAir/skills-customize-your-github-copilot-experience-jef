from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task API")


tasks = [
    {"id": 1, "title": "Write a plan", "completed": False},
    {"id": 2, "title": "Review code", "completed": True},
]


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class Task(TaskCreate):
    id: int


@app.get("/tasks")
async def get_tasks():
    return tasks


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": task.completed,
    }
    tasks.append(new_task)
    return new_task


# TODO: Add GET /tasks/{task_id}
# TODO: Add PUT or PATCH to update a task
# TODO: Add DELETE /tasks/{task_id}
# TODO: Add validation for missing tasks with 404 responses
