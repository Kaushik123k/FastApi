# app/routers/clock_in.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import ClockInCreate, ClockIn
from app.crud import clock_in

router = APIRouter()

@router.post("/clock-in", response_model=ClockIn)
async def create_clock_in(clock_in: ClockInCreate):
    return await clock_in.create_clock_in(clock_in)

@router.get("/clock-in/{id}", response_model=ClockIn)
async def read_clock_in(id: str):
    return await clock_in.read_clock_in(id)

# Add other route handlers for update, delete, and filter.
