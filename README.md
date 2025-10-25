# 🌍 AtlasVoyager

> **From viral shorts to real-world adventures**

AtlasVoyager helps you discover filming locations from YouTube videos using AI-powered geolocation and provides instant travel planning information.

**NewHacks 2025 Project**

## 🎯 What It Does

1. 📹 **Paste a YouTube URL** (shorts, videos, reels)
2. 🤖 **AI identifies the location** using Geo-CLIP computer vision
3. 🗺️ **Interactive map** shows where it was filmed
4. ✨ **Get travel info** - costs, attractions, tips via Gemini AI
5. 💾 **Save trips** for future planning

## 🛠️ Tech Stack

- **Frontend:** React + Vite, Leaflet.js
- **Backend:** FastAPI (Python)
- **ML/AI:** Geo-CLIP (DigitalOcean GPU), Gemini API
- **Database:** MongoDB Atlas
- **APIs:** YouTube Data API

## 📁 Project Structure

```
atlas-voyager/
│
├── frontend/              # React application
│   ├── src/
│   │   ├── components/    # UI components
│   │   ├── pages/         # Input & Output pages
│   │   ├── hooks/         # Custom React hooks
│   │   └── utils/         # API helpers
│   └── package.json
│
├── backend/               # FastAPI server
│   ├── main.py           # App entry point
│   ├── routes/           # API endpoints
│   ├── services/         # Business logic
│   └── models/           # Data models
│
├── GeoCLIP/              # Geo-CLIP inference service
│   ├── main.py
│   ├── routes/
│   └── services/
│
└── docs/                 # Documentation
    ├── architecture.md
    ├── api_endpoints.md
    └── project_overview.md
```

## 🚀 Quick Start

### Prerequisites

- Node.js 18+
- Python 3.9+
- MongoDB Atlas account
- API keys (YouTube, Gemini)

### Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd atlas-voyager
```

2. **Setup environment variables**
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. **Start the backend**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

4. **Start the frontend**
```bash
cd frontend
npm install
npm run dev
```

5. **Start Geo-CLIP service**
```bash
cd GeoCLIP
pip install -r requirements.txt
python main.py
```

### Using Docker Compose (Alternative)

```bash
docker-compose up
```

## 📚 Documentation

- [Architecture Overview](docs/architecture.md)
- [API Endpoints](docs/api_endpoints.md)
- [Project Overview](docs/project_overview.md)

## 🎓 Built For

**NewHacks 2025** - [DevPost](https://newhacks-2025.devpost.com/)

**Sponsor Technologies:**
- DigitalOcean Gradient (GPU Infrastructure)
- MongoDB Atlas (Database)
- Google Gemini API (AI Summaries)

## 🤝 Contributing

This is a hackathon project. Feel free to fork and experiment!

## 📄 License

MIT License

## 🙏 Acknowledgments

- [Geo-CLIP](https://github.com/VicenteVivan/geo-clip) by Vicente Vivanco
- NewHacks 2025 organizers and sponsors
