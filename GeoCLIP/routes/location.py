from fastapi import APIRouter, File, UploadFile, HTTPException
from services.locate import get_coordinates_from_image
import logging

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/locate")
async def locate_image(file: UploadFile = File(...)):
    """
    Receives an image file and returns the predicted coordinates.
    """
    try:
        logger.info(f"Received file: {file.filename}")
        contents = await file.read()
        logger.info(f"File size: {len(contents)} bytes")
        
        coordinates = get_coordinates_from_image(contents)
        
        if coordinates:
            logger.info(f"Predicted coordinates: {coordinates}")
            return coordinates
        else:
            logger.error("Could not predict coordinates from image.")
            raise HTTPException(status_code=400, detail="Could not predict coordinates from image.")
    except Exception as e:
        logger.exception("An error occurred during image processing.")
        raise HTTPException(status_code=500, detail=str(e))
