# Gemini AI route handlers
from fastapi import APIRouter

router = APIRouter(prefix="/api/gemini", tags=["gemini"])


@router.post("/summarize")
async def generate_summary():
    """Generate location summary and travel tips"""
    pass
