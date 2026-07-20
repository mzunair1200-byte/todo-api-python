from fastapi import FastAPI
from httpx import get

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

