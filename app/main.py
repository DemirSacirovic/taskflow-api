from app.api.tasks import router as tasks_router
from fastapi import FastAPI
from app.api.auth import router as auth_router

app = FastAPI(title="TaskFlow")

@app.get("/")
def root():
    return {"message": "TaskFlow API", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(auth_router)
app.include_router(tasks_router)
