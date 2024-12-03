from fastapi import FastAPI
from app.routes import student_routes

app = FastAPI()

# Include API routes
app.include_router(student_routes)

@app.get("/")
def root():
    return {"message": "Welcome to the Student Management System!"}
