from fastapi import APIRouter
from src.api.shemas.task import CreateTask, TaskPartialUpdate

router_task_v1 = APIRouter(prefix="/task/v1", tags=["task | v1"])


@router_task_v1.get("/{user_id}")
async def get_tasks(user_id: int):
    ...


@router_task_v1.post("/create/{user_id}")
async def create_task(user_id: int, task: CreateTask):
    ...


@router_task_v1.patch("/description/{task_id}")
async def refactor_description(task_id: int, task: TaskPartialUpdate):
    ...


@router_task_v1.delete("/{user_id}/{task_id}")
def delete_task(user_id: int, task_id: int):
    ...
