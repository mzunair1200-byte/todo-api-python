from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel

class Task(BaseModel):
    title:str
    id:int
    description:str
    completed:bool
app = FastAPI()

@app.get("/")
def root():
    return {
        "Name":"Taskapi",
        "Version":"1.0.0",
        "endpoint":["/task"]
    }
@app.get("/health")
def health():
    return {
        "status":"ok"
    }
# 1.our in memory database with three exmaple tasks
tasks=[
    {"id":1,"title":"Task 1","description":"This is task 1","completed":False},
    {"id":2,"title":"Task 2","description":"This is task 2","completed":False},
    {"id":3,"title":"Task 3","description":"This is task 3","completed":False}
]
@app.get("/task")
def get_task():
    return tasks

@app.get("/task/{task_id}")
def get_task_by_id(task_id:int):    
    
    for task in tasks:
        if task["id"]==task_id:
            return task
    return {"error":"Task not found"}

@app.get("/healthcheck")
def healthcheck():
    return {"status":"ok"}

@app.post("/task", status_code=status.HTTP_201_CREATED)
def create_task(task:Task):
    new_task=task.model_dump()
    new_task["id"]=len(tasks)+1
    tasks.append(new_task)
    return new_task

@app.put("/task/{task_id}")
def update_task(task_id:int, task:Task):
    for t in tasks:
        if t["id"]==task_id:
            t.update(task.model_dump())
            return t
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

@app.delete("/task/{task_id}")
def delete_task(task_id:int):
    for t in tasks:
        if t["id"]==task_id:
            tasks.remove(t)
            return {"message":"Task deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")