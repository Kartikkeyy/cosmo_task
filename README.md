# Student Management System

This project is a backend application for managing student records, built using FastAPI and MongoDB.

## Features
- Create, list, retrieve, update, and delete students
- MongoDB Atlas for database management
- Dockerized for easy deployment

## Setup Instructions
1. Clone the repository.
2. Add your MongoDB Atlas connection string to the `.env` file.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the application: `python -m uvicorn app.main:app --reload`.
5. Access the API at `http://127.0.0.1:8000`.

## Docker Instructions
1. Build the Docker image: `docker build -t student-management .`
2. Run the Docker container: `docker run -p 8000:8000 student-management`.
