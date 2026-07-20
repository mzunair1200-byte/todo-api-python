from fastapi import FastAPI
from httpx import get, post

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
Task=[
    {"id":1,"title":"Task 1","description":"This is task 1","completed":False},
    {"id":2,"title":"Task 2","description":"This is task 2","completed":False},
    {"id":3,"title":"Task 3","description":"This is task 3","completed":False}
]
@app.get("/task")
def get_task():
    return Task

@app.get("/task/{task_id}")
def get_task_by_id(task_id:int):    
    
    for task in Task:
        if task["id"]==task_id:
            return task
    return {"error":"Task not found"}

@app.get("/healthcheck")
def healthcheck():
    return {"status":"ok"}

@app.post("/task")
def create_task(task:dict):
    task["id"]=len(Task)+1
    Task.append(task)
    return task