import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from userbot.events import register
AUTO_PP = os.environ.get("AUTO_PP", "https://telegra.ph/file/88ab9a1b1243f2c100296.jpg")
import asyncio
import shutil
FONT_FILE_TO_USE = "/app/downloads/Antaro.ttf"

@register(outgoing=True, pattern="^.autopp$")
async def autopic(event):
    downloaded_file_name = "./PAPERPLANE/original_pic.png"
    downloader = SmartDL(AUTO_PP, downloaded_file_name, progress_bar=True)
    downloader.start(blocking=False)
    photo = "photo_pfp.png"
    while not downloader.isFinished():
        place_holder = None
    counter = -30
    while True:
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        file_test = im.rotate(counter, expand=False).save(photo, "PNG")
        current_time = datetime.now().strftime("DATE : %d.%m.%y\nTIME : %H:%M:%S")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 35)
        drawn_text.text((200, 250), current_time, font=fnt, fill=(255, 255, 0))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            counter -= 30
            await asyncio.sleep(60)
        except:
            return
