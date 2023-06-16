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
    return tasks
@app.post("/tasks")

def create_tasks(task: Task):
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    for tarea in task:
        if tarea.id == task_id:
            tarea.title = task.title
            tarea.description = task.description
            tarea.completed = task.completed
            return tarea
    return {"message" : "tarea no encontrada"} 
             
@app.delete("/tasks/{task_id}")
def delete_tasks(task_id: int):
    for tarea in tasks:
        if tarea.id == task_id:
            tasks.remove(tarea)
            return {"message": "tarea eliminada"}
    return {"message": "tarea no encontrada"}