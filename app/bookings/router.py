from fastapi import APIRouter

from app.database import async_session_maker

router = APIRouter(
    prefix="/bookings",
    tags=['Бронирования'],
)

@router.get("")
async def get_bookings():
    pass

