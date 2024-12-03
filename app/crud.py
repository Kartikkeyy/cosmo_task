from bson import ObjectId
from app.config import database

# Helper function to format ObjectId
def format_student(student):
    student["_id"] = str(student["_id"])
    return student

async def create_student(student_data):
    result = await database.db.students.insert_one(student_data)
    return str(result.inserted_id)

async def list_students(filters):
    query = {key: value for key, value in filters.items() if value is not None}
    students = await database.db.students.find(query).to_list(100)
    return [format_student(student) for student in students]

async def fetch_student(student_id):
    student = await database.db.students.find_one({"_id": ObjectId(student_id)})
    return format_student(student) if student else None

async def update_student(student_id, update_data):
    result = await database.db.students.update_one(
        {"_id": ObjectId(student_id)}, {"$set": update_data}
    )
    return result.matched_count > 0

async def delete_student(student_id):
    result = await database.db.students.delete_one({"_id": ObjectId(student_id)})
    return result.deleted_count > 0
