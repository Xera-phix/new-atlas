# AtlasVoyager - Project Overview

## 🎯 Pitch

**"From viral shorts to real-world adventures"**

Users paste a YouTube short link → AI identifies where it was filmed → shows interactive map + location summary → provides trip planning info (costs, attractions) → save trips for later.

## 🏆 Hackathon: NewHacks 2025

**Sponsors/Tech Used:**
- DigitalOcean Gradient (GPU inference for Geo-CLIP)
- MongoDB Atlas (data storage & caching)
- Google Gemini API (AI summaries)
- YouTube Data API (video metadata)

## 💡 The Problem

People see beautiful places in YouTube shorts/reels but have no easy way to:
1. Find out WHERE it was filmed
2. Get travel information about that location
3. Plan a trip there

## ✨ Our Solution

AtlasVoyager uses computer vision (Geo-CLIP) + AI to automatically:
1. Identify filming locations from video frames
2. Display them on an interactive map
3. Provide travel summaries, costs, and nearby attractions
4. Let users save locations for future trips

## 🛠️ Tech Stack

### Frontend
- React + Vite
- Leaflet.js (maps)
- Modern, responsive UI

### Backend
- FastAPI (Python)
- YouTube Data API
- Gemini AI API
- MongoDB Atlas

### ML Infrastructure
- **Geo-CLIP** model on DigitalOcean GPU
- Frame extraction with OpenCV
- Multimodal geolocation inference

## 📊 Key Features (MVP)

1. **YouTube URL Input** ⭐⭐⭐⭐⭐
2. **Geo-CLIP Location Detection** ⭐⭐⭐⭐⭐
3. **Interactive Map Display** ⭐⭐⭐⭐
4. **AI-Generated Summary** ⭐⭐⭐⭐
5. **Trip Cost Estimation** ⭐⭐⭐
6. **Save to MongoDB** ⭐⭐

---

## 🧩 MVP Breakdown

| Feature | Owner | Description | Priority |
| --- | --- | --- | --- |
| YouTube link input + validation | Frontend dev | Textbox + submit button | ⭐⭐⭐⭐ |
| Fetch YouTube video data | Backend dev | Use YouTube API to get metadata | ⭐⭐⭐⭐ |
| Run Geo-CLIP location inference | ML/backend dev | Deploy model on DigitalOcean GPU | ⭐⭐⭐⭐⭐ |
| Display location on map | Frontend dev | Use Leaflet/Google Maps | ⭐⭐⭐⭐ |
| Display AI summary from Gemini | Backend + frontend | Short blurb under the map | ⭐⭐⭐ |
| Save result to MongoDB Atlas | Backend dev | Cache location + summary | ⭐⭐ |
| Nice UI polish for demo | Frontend + design | Clean card layout + gradient theme | ⭐⭐ |

---

## 🕒 Suggested Hackathon Timeline

### **Day 1 (Ideation + Setup)**

- ✅ Finalize idea + pitch wording
- ✅ Setup repos + environment (React, FastAPI, Atlas cluster, DO account)
- ✅ Get YouTube API + Gemini API keys working
- ✅ Confirm Geo-CLIP runs locally / on DigitalOcean

### **Day 2 (Build)**

- 🧠 Backend: YouTube → Geo-CLIP → Gemini → Atlas
- 💻 Frontend: Input → map display → summary view
- 🔄 Connect endpoints (frontend calls backend API)

### **Day 3 (Polish + Pitch)**

- ✨ Add visuals + animations (React transitions, maybe framer-motion)
- 🎥 Record a video demo (YouTube clip → output location)
- 🧑‍🏫 Finalize slides + explain DigitalOcean Gradient integration

---

## 🧠 DigitalOcean Gradient Integration Ideas

Judges want to see you *use their AI infra*. You can:

- Host **Geo-CLIP** inference on a **GPU Droplet or serverless endpoint**
- Show a simple CLI or REST call hitting your hosted model ("This model is running on DigitalOcean Gradient")
- Mention you leveraged **Gradient's GPU runtime for fast multimodal inference**

---

## 💡 Bonus Ideas (if time allows)

- "Trip Planner" page → fetch flight/hotel cost estimates (use Gemini or open travel API)
- "Save to Favorites" → store planned trips in user profile
- Chrome extension → right-click "Find this location"
- Leaderboard of most-searched landmarks
- Social share ("Find this reel in real life!")

## 🎓 What We Learned

- Deploying ML models on GPU infrastructure
- Integrating multiple APIs (YouTube, Gemini, Geo-CLIP)
- Building real-time inference pipelines
- Caching strategies for faster re-searches

## 🚀 Future Enhancements

- Chrome extension for right-click "Find this location"
- Social sharing features
- Multi-location trip planning
- User accounts and profiles
- Flight/hotel booking integration

## 👥 Team

[Add your team members here]

## 📝 Demo Script

1. Show a popular travel YouTube short
2. Paste URL into AtlasVoyager
3. Wait 3-5 seconds → location identified
4. Map appears with marker
5. AI summary shows location details
6. Trip cost estimate displayed
7. Save to favorites

## 🔗 Links

- GitHub Repo: [Your repo link]
- Live Demo: [Deployment link]
- DevPost: https://newhacks-2025.devpost.com/
- Geo-CLIP: https://github.com/VicenteVivan/geo-clip
