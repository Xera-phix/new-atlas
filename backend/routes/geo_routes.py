# Geo-CLIP location detection route handlers
from fastapi import APIRouter

router = APIRouter(prefix="/api/geo", tags=["geolocation"])


@router.post("/locate")
async def locate_from_image():
    """Get geographic coordinates from image using Geo-CLIP"""
    pass
