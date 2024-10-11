# app/crud/items.py
from app.database import items_collection
from app.schemas import ItemCreate, Item
from bson import ObjectId
from datetime import datetime

async def create_item(item: ItemCreate):
    item_data = item.dict()
    item_data["insert_date"] = datetime.utcnow()
    result = await items_collection.insert_one(item_data)
    item_data["_id"] = str(result.inserted_id)
    return item_data

# Similarly, add functions for read, update, delete, and filter.
