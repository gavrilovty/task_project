from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class UserId(BaseModel):
    """
    Обёртка-схема для передачи user_id — может использоваться
    отдельно в ручках, где требуется только идентификатор пользователя.
    """
    user_id: Optional[int] = None


class CreateTaskBase(BaseModel):
    """
    Базовая схема для создания задачи. Используется как основа
    для полной или частичной передачи данных о задаче.
    """
    title: str  # Название задачи
    user_id: int  # ID пользователя, к которому относится задача
    description: Optional[str] = None  # Описание задачи
    due_date: Optional[datetime] = None  # Срок исполнения


class CreateTask(CreateTaskBase):
    """
    Схема для создания новой задачи (POST).
    Наследуется от CreateTaskBase, но может быть доопределена.
    """
    title: str  # Повторно указываем, если нужно переопределить правила или документацию


class TaskPartialUpdate(CreateTask):
    """
    Схема для частичного обновления задачи (PATCH).
    Поля могут быть опущены, если не требуется их изменение.
    """
    title: Optional[str] = None  # Можно не передавать или передать None
