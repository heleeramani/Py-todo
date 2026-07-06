from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate

def get_all(db: Session) -> list[Todo]:
    return db.query(Todo).all()

def get_by_id(db: Session, todo_id: int) -> Todo | None:
    return db.query(Todo).filter(Todo.id == todo_id).first()

def create(db: Session, todo_data: TodoCreate) -> Todo:
    # Convert API data into a database object
    new_todo = Todo(**todo_data.model_dump())
    # Add to session, commit to save, and refresh to get updated data (like ID)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def update(db: Session, todo: Todo, todo_data: TodoUpdate) -> Todo:
    update_fields = todo_data.model_dump(exclude_unset=True)
    for field, value in update_fields.items():
        setattr(todo, field, value)
    db.commit()
    db.refresh(todo)
    return todo

def delete(db: Session, todo: Todo) -> None:
    db.delete(todo)
    db.commit()