from typing import Dict, List

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    completed: bool = False


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


app = FastAPI(title="To-Do List API", version="1.0.0")

_tasks: Dict[int, Task] = {}
_next_id = 1


def _seed_data() -> None:
    global _next_id
    initial_tasks = [
        {"title": "Buy groceries", "description": "Pick up milk, bread, and eggs", "completed": False},
        {"title": "Write report", "description": "Prepare the weekly project summary", "completed": True},
        {"title": "Call the dentist", "description": "Book a dental appointment", "completed": False},
    ]
    for task_data in initial_tasks:
        task = Task(id=_next_id, **task_data)
        _tasks[task.id] = task
        _next_id += 1


_seed_data()


@app.get("/", tags=["root"])
def root() -> dict:
    return {
        "name": "To-Do List API",
        "version": "1.0.0",
        "endpoints": ["/", "/health", "/task", "/task/{task_id}"],
    }


@app.get("/health", tags=["health"])
def health_check() -> dict:
    return {"status": "ok"}


@app.get("/task", response_model=List[Task], tags=["tasks"])
def get_tasks() -> List[Task]:
    return list(_tasks.values())


@app.get("/task/{task_id}", response_model=Task, tags=["tasks"])
def get_task(task_id: int) -> Task:
    task = _tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@app.post("/task", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["tasks"])
def create_task(task_data: TaskCreate) -> Task:
    global _next_id
    task = Task(id=_next_id, title=task_data.title, description=task_data.description, completed=task_data.completed)
    _tasks[task.id] = task
    _next_id += 1
    return task


@app.put("/task/{task_id}", response_model=Task, tags=["tasks"])
def update_task(task_id: int, task_data: TaskUpdate) -> Task:
    task = _tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    if task_data.title is not None:
        task.title = task_data.title
    if task_data.description is not None:
        task.description = task_data.description
    if task_data.completed is not None:
        task.completed = task_data.completed

    _tasks[task_id] = task
    return task


@app.delete("/task/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["tasks"])
def delete_task(task_id: int) -> None:
    if task_id not in _tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    _tasks.pop(task_id)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("ai_version:app", host="127.0.0.1", port=8000, reload=False)
