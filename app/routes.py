from fastapi import APIRouter, HTTPException
from app.models import Student, UpdateStudent
from app.crud import create_student, list_students, fetch_student, update_student, delete_student

student_routes = APIRouter(prefix="/students", tags=["Students"])

@student_routes.post("/", status_code=201)
async def create(student: Student):
    student_id = await create_student(student.dict())
    return {"id": student_id}

@student_routes.get("/")
async def list_all(country: str = None, age: int = None):
    filters = {"address.country": country, "age": {"$gte": age} if age else None}
    students = await list_students(filters)
    return {"data": students}

@student_routes.get("/{student_id}")
async def retrieve(student_id: str):
    student = await fetch_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@student_routes.patch("/{student_id}", status_code=204)
async def update(student_id: str, updates: UpdateStudent):
    success = await update_student(student_id, updates.dict(exclude_unset=True))
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")

@student_routes.delete("/{student_id}", status_code=200)
async def delete(student_id: str):
    success = await delete_student(student_id)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
