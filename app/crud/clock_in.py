# app/crud/clock_in.py
from app.database import clock_in_collection
from app.schemas import ClockInCreate, ClockIn
from bson import ObjectId
from datetime import datetime

async def create_clock_in(clock_in: ClockInCreate):
    clock_in_data = clock_in.dict()
    clock_in_data["insert_datetime"] = datetime.utcnow()
    result = await clock_in_collection.insert_one(clock_in_data)
    clock_in_data["_id"] = str(result.inserted_id)
    return clock_in_data

# Similarly, add functions for read, update, delete, and filter.
