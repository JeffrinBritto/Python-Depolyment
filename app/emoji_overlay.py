from PIL import Image, ImageDraw, ImageFont
from fastapi import UploadFile
import io

async def add_emoji_to_image(file: UploadFile, emoji: str) -> io.BytesIO:
    image = Image.open(file.file).convert("RGBA")
    draw = ImageDraw.Draw(image)

    font_size = int(min(image.size) * 0.1)

    # Load a default font (emoji support varies by OS)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    text_width, text_height = draw.textsize(emoji, font=font)
    position = (image.width - text_width - 10, image.height - text_height - 10)

    draw.text(position, emoji, font=font, fill=(255, 255, 255, 255))

    byte_io = io.BytesIO()
    image.save(byte_io, format="PNG")
    byte_io.seek(0)

    return byte_io
