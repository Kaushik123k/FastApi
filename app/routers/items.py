# app/routers/items.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import ItemCreate, Item
from app.crud import items

router = APIRouter()

@router.post("/items", response_model=Item)
async def create_item(item: ItemCreate):
    return await items.create_item(item)

@router.get("/items/{id}", response_model=Item)
async def read_item(id: str):
    return await items.read_item(id)

# Add other route handlers for update, delete, filter, and aggregation.
