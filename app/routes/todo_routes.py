from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse
from app.schemas.ai import NaturalLanguageInput
from app.services import todo_service, ai_service

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.get("/", response_model=list[TodoResponse])
def list_todos(db: Session = Depends(get_db)):
    return todo_service.list_todos(db)


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    return todo_service.get_todo(db, todo_id)


@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return todo_service.create_todo(db, todo)


@router.patch("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    return todo_service.update_todo(db, todo_id, todo)


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_service.delete_todo(db, todo_id)
    
    
@router.post("/smart", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo_from_text(payload: NaturalLanguageInput, db: Session = Depends(get_db)):
    parsed = ai_service.parse_task(payload.text, payload.timezone)
    todo_data = TodoCreate(
        title=parsed.title,
        description=parsed.description,
    )
    todo = todo_service.create_todo(db, todo_data)
    todo.is_ai_generated = True

    if parsed.due_date or parsed.priority:
        todo.due_date = parsed.due_date
        todo.priority = parsed.priority
    db.commit()
    db.refresh(todo)

    return todo