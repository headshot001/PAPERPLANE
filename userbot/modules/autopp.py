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
from userbot import CMD_HELP, bot
url = 'https://raw.githubusercontent.com/Ayush1311/PAPERPLANE/master/Antaro.ttf'
urllib.request.urlretrieve(url, './Antaro.ttf')
FONT_FILE_TO_USE = "./Antaro.ttf"
url1 = 'https://telegra.ph/file/d3048ee6593a0bcb327a3.png'
urllib.request.urlretrieve(url1, './original_pic.png')

@register(outgoing=True, pattern="^.autopp$")
async def autopic(event):
    while True:
        downloaded_file_name = "./original_pic.png"
        photo = "./new_photo.png"
        shutil.copy(downloaded_file_name, photo)
        LT = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        OT = LT.strftime("root@ayush:~# python3\n\n>>>import datetime\n\n>>>localtime = datetime.datetime.now()\n\n>>>while True :\n\n...     print(' ',localtime)\n\n...     print(' ','HAVE A NICE DAY !')\n\n...     sleep(60)\n\n...else :\n\n...     break\n\n>>> %d.%m.%y %H:%M\n\n>>> HAVE A NICE DAY !")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 25)
        drawn_text.text((40, 80), OT, align='left', font=fnt, fill="red")
        img.save(photo)
        file = await event.client.upload_file(photo) 
        try:
            lim = 1
            pfplist = await bot(GetUserPhotosRequest(user_id=event.from_id, offset=0, max_id=0, limit=lim))
            input_photos = []
            for sep in pfplist.photos:
                input_photos.append(InputPhoto(id=sep.id, access_hash=sep.access_hash, file_reference=sep.file_reference))
            await bot(DeletePhotosRequest(id=input_photos))
            await event.client(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(photo)
            await asyncio.sleep(60)
            
        except:
            return

    


CMD_HELP.update({
"autoname":
"A module to show a runnig timer in the user profile picture"
})
