from fastapi import APIRouter
from sqlalchemy import select

from app.bookings.dao import BookingsDAO

from app.bookings.schemas import SchemaBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)

@router.get("")
async def get_bookings() -> list[SchemaBooking]:
    return await BookingsDAO.find_all()
