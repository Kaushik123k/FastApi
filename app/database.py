# app/database.py
from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_DETAILS = os.getenv("MONGO_DETAILS", "mongodb://localhost:27017")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.fastapi_db

items_collection = database.get_collection("items")
clock_in_collection = database.get_collection("clock_in_records")
