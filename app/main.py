from fastapi import FastAPI, Query, Depends
from datetime import date
from pydantic import BaseModel
from dataclasses import dataclass

app = FastAPI()

class SHotel(BaseModel):
    address: str
    name: str
    stars: int
    has_spa: bool


@dataclass
class HotelSearchArgs():
    location: str
    date_from: date
    date_to: date
    has_spa: bool | None = None
    stars: int | None = Query(None, ge=1, le=5)


@app.get("/hotels")
def get_hotels(
    search_args: HotelSearchArgs = Depends() # чтобы в swagger поля датакласса улетели
    ) -> list[SHotel]:
    
    hotels = [
        {"address": "sdfsdf", "name": "awdawd", "stars": 4, "has_spa": True}
    ]
    return hotels

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

@app.post("/bookings")
def add_booking(booking: SBooking):
    pass