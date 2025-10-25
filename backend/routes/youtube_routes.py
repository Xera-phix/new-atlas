# YouTube API route handlers
from fastapi import APIRouter

router = APIRouter(prefix="/api/youtube", tags=["youtube"])


@router.post("/analyze")
async def analyze_video():
    """Extract metadata from YouTube video"""
    pass
