from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")

class Task(BaseModel):
    id : int
    title: str
    description: str
    completed: bool

tasks = []

@app.get("/tasks")

def get_tasks():
    return Tasks
@app.post("/tasks")

def create_tasks(task: Task):
    tasks.append(task)
    return task

