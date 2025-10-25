# AtlasVoyager API Endpoints

Base URL: `http://localhost:8000`

## Health & Status

### `GET /`
Welcome message

**Response:**
```json
{
  "message": "Welcome to AtlasVoyager API"
}
```

### `GET /health`
Health check

**Response:**
```json
{
  "status": "healthy"
}
```

## YouTube Analysis

### `POST /api/youtube/analyze`
Analyze YouTube video and extract metadata

**Request Body:**
```json
{
  "video_url": "https://youtube.com/shorts/xxxxx"
}
```

**Response:**
```json
{
  "video_id": "xxxxx",
  "title": "Video Title",
  "description": "Video description",
  "thumbnail_url": "https://...",
  "frame_data": "base64_encoded_frame"
}
```

## Geolocation

### `POST /api/geo/locate`
Get geographic coordinates from image using Geo-CLIP

**Request Body:**
```json
{
  "image_data": "base64_encoded_image",
  "video_id": "xxxxx"
}
```

**Response:**
```json
{
  "latitude": 40.7128,
  "longitude": -74.0060,
  "confidence": 0.92,
  "location_name": "New York, USA"
}
```

## AI Summary

### `POST /api/gemini/summarize`
Generate location summary and travel information

**Request Body:**
```json
{
  "location": {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "name": "New York, USA"
  },
  "video_context": "Video title and description"
}
```

**Response:**
```json
{
  "summary": "This location appears to be...",
  "attractions": ["Statue of Liberty", "Central Park"],
  "estimated_cost": {
    "flight": "$400-600",
    "hotel": "$150-300/night",
    "daily_budget": "$100-200"
  }
}
```

## Trip Management

### `GET /api/trips`
Get all saved trips

**Query Parameters:**
- `user_id` (optional): Filter by user

**Response:**
```json
{
  "trips": [
    {
      "id": "trip_id",
      "video_url": "...",
      "location": {...},
      "created_at": "2025-10-25T..."
    }
  ]
}
```

### `POST /api/trips`
Save a new trip

**Request Body:**
```json
{
  "video_url": "https://...",
  "location": {...},
  "summary": {...},
  "user_id": "optional_user_id"
}
```

**Response:**
```json
{
  "id": "trip_id",
  "success": true,
  "message": "Trip saved successfully"
}
```

### `GET /api/trips/{trip_id}`
Get specific trip by ID

**Response:**
```json
{
  "id": "trip_id",
  "video_url": "...",
  "location": {...},
  "summary": {...},
  "created_at": "..."
}
```
