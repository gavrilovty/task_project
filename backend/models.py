from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False
    due_date: Optional[datetime] = None

class UserId(TaskBase):
    user_id: int


class Task(TaskBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True



class TaskPartialUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    due_date: Optional[datetime] = None