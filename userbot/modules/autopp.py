# PLUGIN RE-ESTABLISHED BY @AyushChatterjee, Original Creator is @Spechide

import os
import datetime
import time
from PIL import Image, ImageDraw, ImageFont
from telethon.tl import functions
from userbot.events import register
import asyncio
import shutil
import pytz 
import urllib.request
from telethon import events
from userbot import CMD_HELP
url = 'https://raw.githubusercontent.com/Ayush1311/PAPERPLANE/master/Antaro.ttf'
url1 = 'https://telegra.ph/file/bd2d8bae73546db5719db.jpg'
urllib.request.urlretrieve(url, './Antaro.ttf')
urllib.request.urlretrieve(url1, './original_pic.png')
FONT_FILE_TO_USE = "./Antaro.ttf"
downloaded_file_name = "./original_pic.png"
photo = "./new_photo.png"


@register(outgoing=True, pattern="^.autopp$")
async def autopic(event):
    while True:
        shutil.copy(downloaded_file_name, photo)
        LT = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        OT = LT.strftime("root@ayush:~# python3\n\n>>>import datetime\n\n>>>localtime = datetime.datetime.now()\n\n>>>while True :\n\n...     print(' ',localtime)\n\n...     print(' ','HAVE A NICE DAY !')\n\n...else :\n\n...     break\n\n>>> %d.%m.%y %H:%M\n\n>>> HAVE A NICE DAY !")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 25)
        drawn_text.text((40, 80), OT, font=fnt, fill="red")
        img.save(photo)
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(photo)
            await asyncio.sleep(60)
        except:
            return

CMD_HELP.update({
"autoname":
"A module to show a runnig timer in the user profile picture"
})
