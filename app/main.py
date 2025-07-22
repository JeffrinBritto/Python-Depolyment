from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import router as emoji_router

app = FastAPI(title="Emoji Overlay Service")

# Mount static folder to serve HTML/CSS/JS
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")

# Include API routes
app.include_router(emoji_router, prefix="/api")
