# AtlasVoyager Backend - Main Entry Point
# FastAPI application for YouTube location detection

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AtlasVoyager API", version="1.0.0")

# CORS configuration for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to AtlasVoyager API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


# Import and include routers here
# from routes import youtube_routes, gemini_routes, geo_routes, db_routes
# app.include_router(youtube_routes.router)
# app.include_router(gemini_routes.router)
# app.include_router(geo_routes.router)
# app.include_router(db_routes.router)
