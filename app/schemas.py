# app/schemas.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, date

class ItemBase(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: date

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: str
    insert_date: datetime

class ClockInBase(BaseModel):
    email: str
    location: str

class ClockInCreate(ClockInBase):
    pass

class ClockIn(ClockInBase):
    id: str
    insert_datetime: datetime
