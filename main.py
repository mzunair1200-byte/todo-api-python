from fastapi import FastAPI
from httpx import get

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello world"}

