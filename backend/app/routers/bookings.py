from fastapi import APIRouter, Depends

from app.services.booking_service import BookingService
from app.dependencies.container import get_booking_service


router = APIRouter(
    prefix="/api/bookings",
    tags=["Bookings"]
)


@router.post("/")
def create_booking(
    service: BookingService = Depends(get_booking_service)
):
    return service.create_booking()