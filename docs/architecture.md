# AtlasVoyager System Architecture

## Overview

AtlasVoyager is a web application that identifies filming locations from YouTube videos using AI and provides travel planning information.

**Pitch:** Users paste a YouTube short link → AI identifies where it was filmed → shows map + trip summary (costs, nearby attractions, etc.) → user can save or plan their trip.

---

## ⚙️ Tech Architecture

### **Frontend (React)**

- **Input Page:** User pastes a YouTube link → clicks *Find Location*
- **Output Page:** Map view (Leaflet.js / Google Maps embed) + location summary + trip cost estimate
- **Optional:** "Save for later" or "Add to trip" feature → stored in Atlas

---

### **Backend (FastAPI)**

**Core flow:**

1. **Input:** YouTube link → extract metadata with **YouTube Data API**
    - video title, description, transcript (if available), and thumbnail
2. **Geo-CLIP Model (DigitalOcean GPU instance):**
    - frame extraction (from video or thumbnail)
    - pass through CLIP → compare embeddings with global geolocation dataset → output coordinates
3. **Gemini API:**
    - Summarize the scene or generate travel tips ("This clip was shot in Santorini — a popular Greek island known for sunsets.")
    - Optional: Estimate cost (flight + hotel + local transport using rough data)
4. **Atlas (MongoDB Atlas):**
    - Store user queries, location metadata, and embeddings for caching (so re-searches are faster)

---

## System Flow

```
┌─────────────────────────────┐
│         Frontend            │
│  (React + Vite / Next.js)   │
│─────────────────────────────│
│  • YouTube URL input box    │
│  • "Find Location" button   │
│  • Map + AI Summary Display │
│  • Trip cost + save options │
└────────────┬────────────────┘
             │  (REST API call)
             ▼
┌─────────────────────────────┐
│          Backend            │
│  (FastAPI / Node.js)        │
│─────────────────────────────│
│  1️⃣ YouTube Data API call  │
│     → get title, desc, vid  │
│                             │
│  2️⃣ Geo-CLIP inference     │
│     → extract frame/embed   │
│     → predict coordinates   │
│                             │
│  3️⃣ Gemini API summary     │
│     → "Looks like Bali"     │
│     → travel tips/cost est. │
│                             │
│  4️⃣ Save to Mongo Atlas DB │
│     → user + video metadata │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│      MongoDB Atlas          │
│─────────────────────────────│
│  • Stores:                 │
│    - video metadata        │
│    - geo embeddings        │
│    - user saved trips      │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  DigitalOcean Gradient AI   │
│─────────────────────────────│
│  • Hosts Geo-CLIP model     │
│  • Runs GPU inference       │
│  • Sends results to backend │
└─────────────────────────────┘
```

## Technology Stack

### Frontend
- **React** with Vite
- **Leaflet.js** for map visualization
- **Axios** for API calls

### Backend
- **FastAPI** (Python)
- **YouTube Data API** for video metadata
- **Gemini API** for AI summaries
- **MongoDB Atlas** for data storage

### ML/AI Infrastructure
- **Geo-CLIP** model hosted on DigitalOcean GPU
- **Frame extraction** using OpenCV

## Data Flow

**Flow summary:**

1. User pastes YouTube link → frontend sends to backend.
2. Backend fetches video metadata from YouTube API.
3. A frame/thumbnail is sent to Geo-CLIP model (running on DigitalOcean GPU) → returns coordinates.
4. Gemini API summarizes the location + suggests trip info.
5. Backend stores everything in MongoDB Atlas and returns results to frontend.
6. Frontend displays map + AI summary + estimated trip cost.

### Detailed Steps

1. **User Input** → User pastes YouTube URL
2. **Metadata Extraction** → Backend fetches video info via YouTube API
3. **Frame Extraction** → Backend extracts video frame/thumbnail
4. **Location Inference** → Frame sent to Geo-CLIP on DigitalOcean
5. **Coordinates Returned** → Geo-CLIP returns lat/long
6. **AI Enhancement** → Gemini generates location summary
7. **Caching** → Results stored in MongoDB Atlas
8. **Display** → Frontend shows map + summary + trip info
