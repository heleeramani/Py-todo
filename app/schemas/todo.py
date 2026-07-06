from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class NaturalLanguageInput(BaseModel):
    text: str

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None


class TodoResponse(TodoBase):
    id: int
    is_completed: bool
    due_date: Optional[datetime] = None
    priority: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    # 👉 It allows Pydantic to convert database objects (like SQLAlchemy models) into JSON response schemas by reading their attributes.

    # Without it → only works with dicts
    # With it → works with ORM objects too 👍
    model_config = ConfigDict(from_attributes=True)