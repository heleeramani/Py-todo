from fastapi import FastAPI
from app.routes import todo_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Todo API", version="1.0.0")

app.include_router(todo_routes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://to-do-xho1.onrender.com"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}