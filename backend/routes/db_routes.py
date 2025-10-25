# MongoDB Atlas database route handlers
from fastapi import APIRouter

router = APIRouter(prefix="/api/trips", tags=["database"])


@router.get("/")
async def get_trips():
    """Get all saved trips"""
    pass


@router.post("/")
async def save_trip():
    """Save a new trip"""
    pass


@router.get("/{trip_id}")
async def get_trip():
    """Get a specific trip by ID"""
    pass
