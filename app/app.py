from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from app.emoji_overlay import add_emoji_to_image

router = APIRouter()

@router.post("/add-emoji")
async def add_emoji(file: UploadFile = File(...), emoji: str = "😎"):
    result_image = await add_emoji_to_image(file, emoji)
    return StreamingResponse(result_image, media_type="image/png")
