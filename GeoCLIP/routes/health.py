from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Checks the health of the API.
    """
    return {"status": "ok"}
