from fastapi import FastAPI
from routes import location, health

app = FastAPI()

app.include_router(location.router)
app.include_router(health.router)

@app.get("/")
async def root():
    return {"message": "GeoCLIP service is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
