# Service IS:

# ✔ validation logic
# ✔ error handling
# ✔ combining repository calls
# ✔ business rules
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories import todo_repository
from app.schemas.todo import TodoCreate, TodoUpdate
from app.models.todo import Todo


def list_todos(db: Session) -> list[Todo]:
    return todo_repository.get_all(db)


def get_todo(db: Session, todo_id: int) -> Todo:
    todo = todo_repository.get_by_id(db, todo_id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo


def create_todo(db: Session, todo_data: TodoCreate) -> Todo:
    return todo_repository.create(db, todo_data)


def update_todo(db: Session, todo_id: int, todo_data: TodoUpdate) -> Todo:
    todo = get_todo(db, todo_id)  # reuses the 404 check
    return todo_repository.update(db, todo, todo_data)


def delete_todo(db: Session, todo_id: int) -> None:
    todo = get_todo(db, todo_id)
    todo_repository.delete(db, todo)