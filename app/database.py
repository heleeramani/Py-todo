# Connect your app to the database and manage database sessions.

# Imports SQLAlchemy function that creates database connection.
# Think:
# engine = connection bridge
# between app ↔ PostgreSQL.
from sqlalchemy import create_engine


# sessionmaker

# Creates database sessions.
# A session is like:
# temporary conversation with database
# You use session to:
# insert data, update data, delete data, fetch data=
# 
# declarative_base
# Creates base class for all models.
# Example:
# class Todo(Base):
# Without Base, SQLAlchemy cannot recognize models.
from sqlalchemy.orm import sessionmaker, declarative_base

# Imports settings from your config.
from app.config import settings

# This creates database engine.
# Think of engine as:
# main connection manager
# between app and PostgreSQL.
# FastAPI App
#      ↓
# SQLAlchemy Engine
#      ↓
# PostgreSQL
engine = create_engine(settings.database_url)

# This creates a session factory.
# Meaning:
# “Whenever needed, create new database sessions.”

# autocommit=False Database changes are NOT saved automatically.
# autoflush=False Don’t automatically send pending changes to DB.
# bind=engine Use this engine/database connection.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This creates parent class for models.
Base = declarative_base()

# This creates dependency function.
# Purpose:
# Give database session to API routes safely.
def get_db(): 
    # Creates new database session.
    db = SessionLocal()
    try:
        # After request finishes, it resumes.
        yield db
    finally:
        # Closes database session safely.
        db.close()
        
        
    
# for testing write in terminal:
# python3 -c "from app.database import engine; print(engine.connect())"