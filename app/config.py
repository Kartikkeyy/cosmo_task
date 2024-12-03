import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch MongoDB connection details
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")

# Initialize MongoDB client and database
client = AsyncIOMotorClient(MONGO_URI)
database = client[MONGO_DB]
