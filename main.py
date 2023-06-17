from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
app = FastAPI()

@app.get("/")

class Task(BaseModel):
    id : int 
    title: str = Field(max_length=255)
    description: str = Field(max_length=255)
    completed: bool

tasks = []

@app.get("/tasks")
def get_tasks():
    return JSONResponse(content=tasks)

@app.post("/tasks")

def create_tasks(task: Task):
    tasks.append(task)
    return JSONResponse(content={"message":"se ha creado la tarea"})

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    for tarea in task:
        if tarea.id == task_id:
            tarea.title = task.title
            tarea.description = task.description
            tarea.completed = task.completed
            return JSONResponse(content=tarea)
    return JSONResponse(content={"message" : "tarea no encontrada"}) 
             
@app.delete("/tasks/{task_id}")
def delete_tasks(task_id: int):
    for tarea in tasks:
        if tarea.id == task_id:
            tasks.remove(tarea)
            return JSONResponse(content={"message": "tarea eliminada"})
    return JSONResponse(content={"message": "tarea no encontrada"})