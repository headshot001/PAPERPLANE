# PLUGIN RE-ESTABLISHED BY @AyushChatterjee, Original Creator is @Spechide

import os
import datetime
import time
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from userbot.events import register
AUTO_PP = os.environ.get("AUTO_PP", "https://telegra.ph/file/d3048ee6593a0bcb327a3.png")
import asyncio
import shutil
import pytz 
import urllib.request
from telethon import events
from userbot import CMD_HELP
url = 'https://raw.githubusercontent.com/Ayush1311/PAPERPLANE/master/fontfile.ttf'
urllib.request.urlretrieve(url, './fontfile.ttf')
FONT_FILE_TO_USE = "./fontfile.ttf"

@register(outgoing=True, pattern="^.autopp$")
async def autopic(event):
    downloaded_file_name = "./original_pic.png"
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
        LT = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        OT = LT.strftime("root@ayush:~# python3\n\n>>>import datetime\n\n>>>localtime = datetime.datetime.now()\n\n>>>while True :\n\n>>>     print(' ',localtime)\n\n>>>     print(' ','HAVE A NICE DAY !')\n\n>>>else :\n\n>>>     break\n\n>>> %d.%m.%y %H:%M\n\n>>> HAVE A NICE DAY !")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 25)
        drawn_text.text((40, 80), OT, font=fnt, fill="black")
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


CMD_HELP.update({
"autoname":
"A module to show a runnig timer in the user profile picture"
})
