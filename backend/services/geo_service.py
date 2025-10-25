# Geo-CLIP service logic
# Handles communication with Geo-CLIP model on DigitalOcean


class GeoService:
    """Service for location inference using Geo-CLIP"""

    def __init__(self, model_endpoint: str):
        self.model_endpoint = model_endpoint

    async def predict_location(self, image_data):
        """Send image to Geo-CLIP and get coordinates"""
        pass
