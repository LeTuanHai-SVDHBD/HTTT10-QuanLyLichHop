from fastapi import FastAPI

from app.routers.bookings import router as booking_router


app = FastAPI(
    title="HTTT10 - Quản lý lịch họp và đặt phòng"
)


app.include_router(booking_router)


@app.get("/")
def root():
    return {
        "message": "HTTT10 API đang hoạt động"
    }