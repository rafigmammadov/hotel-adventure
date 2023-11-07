from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.bookings.models import Bookings

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)

@router.get("")
async def get_bookings1():
    async with async_session_maker() as session:
        query = select(Bookings)
        result = await session.execute(query)
        return result.mappings().all()

