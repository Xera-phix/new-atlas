# AtlasVoyager Backend

FastAPI backend for YouTube location detection and travel planning.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and fill in your API keys:
```bash
cp ../.env.example .env
```

3. Run the development server:
```bash
uvicorn main:app --reload
```

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `POST /api/youtube/analyze` - Analyze YouTube video
- `POST /api/geo/locate` - Get location from Geo-CLIP
- `POST /api/gemini/summarize` - Generate AI summary
- `GET /api/trips` - Get saved trips
- `POST /api/trips` - Save a trip

## Project Structure

```
backend/
├── main.py              # FastAPI app entry point
├── routes/              # API route handlers
├── services/            # Business logic
├── models/              # Pydantic models
├── requirements.txt     # Python dependencies
└── README.md
```
