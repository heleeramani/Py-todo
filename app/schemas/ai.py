from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class NaturalLanguageInput(BaseModel):
    text: str
    timezone: Optional[str] = "Asia/Kolkata"


class ParsedTodo(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: Optional[str] = None