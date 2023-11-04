from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI()

class SchemaHotel(BaseModel):
    name: str
    address: str
    stars: int

class SchemaGetHotel:

    def __init__(
            self,
            hotel_id: str,
            date_from: date,
            date_to: date,
            has_spa: Optional[bool] = None,
            stars: Optional[int] = Query(None, ge=1, le=5)
                ):
        self.hotel_id = hotel_id
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars

        
@app.get('/hotels/{hotel_id}')
def get_hotels(searching_args: SchemaGetHotel = Depends()):
    return searching_args


class SchemaBookingPost(BaseModel):
    price: int
    date_from: date
    date_to: date


@app.post('/book')
def add_booking(booking: SchemaBookingPost):
    pass