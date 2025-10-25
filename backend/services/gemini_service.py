# Gemini AI service logic
# Handles AI-generated summaries and travel information


class GeminiService:
    """Service for generating AI summaries using Gemini API"""

    def __init__(self, api_key: str):
        self.api_key = api_key

    async def generate_location_summary(self, location_data: dict):
        """Generate travel summary for a location"""
        pass

    async def estimate_trip_cost(self, location: str, origin: str = "USA"):
        """Estimate travel costs"""
        pass
