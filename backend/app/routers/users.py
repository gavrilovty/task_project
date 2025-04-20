from fastapi import FastAPI
from backend.models import UserId, Task, TaskPartialUpdate


app = FastAPI()

data = {}

@app.get("/tasks")
async def get_tasks(user_id: UserId):
    return {"response": 200, "user_id": user_id}


@app.post("/create")
async def create_task(task: Task):
    data[f"{task.user_id}"] = [task.user_id, task.title]
    return {"response": 200, "user_id": task.user_id}

@app.patch("/description")
async def refactor_description(task: TaskPartialUpdate):
    try:
        return {"response": 200}
    except Exception as e:
        print(e)


@app.delete("/tasks/{task_id}")
def delete_task(user_id: int):
    return {"response": 200, "user_id": user_id}