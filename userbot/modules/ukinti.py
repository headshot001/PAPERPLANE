from telethon import events
from datetime import datetime, timedelta
from telethon.tl.types import UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusRecently, ChannelParticipantsKicked, ChatBannedRights
from telethon.tl import functions, types
from time import sleep
import asyncio
from telethon import *
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
from telethon.tl.functions.channels import LeaveChannelRequest

from userbot.events import register
from PIL import Image
import os 


@register(pattern=".kickthefools")
async def _(event):
    if event.fwd_from:
        return
    
    c = 0
    KICK_RIGHTS = ChatBannedRights(until_date=None, view_messages=True)
    UserStatusLongAgo = int(UserStatusLastMonth) + int(UserStatusLastWeek)
    await event.reply("Searching Participant Lists...")
    async for i in event.client.iter_participants(event.chat_id):

        if isinstance(i.status, UserStatusLastMonth):
            status = await event.client(EditBannedRequest(event.chat_id, i, KICK_RIGHTS))
            if not status:
               return
            else:
               c = c + 1
                    
        if isinstance(i.status, UserStatusLastWeek):
            status = await event.client(EditBannedRequest(event.chat_id, i, KICK_RIGHTS))
            if not status:
               return
            else:
               c = c + 1       

        if isinstance(i.status, UserStatusLongAgo):
            status = await event.client(EditBannedRequest(event.chat_id, i, KICK_RIGHTS))
            if not status:
               return
            else:
               c = c + 1
    
    required_string = "Successfully Kicked **{}** users"
    await event.reply(required_string.format(c))


@register(pattern="^/ascii")
async def asciiart(event):
  if event.fwd_from:
     return  
  if not event.from_id:
     await event.reply("Reply To A Image Plox..")
     return
  reply_msg = await event.get_reply_message()
  if not os.path.isdir('./'):
        os.makedirs('./')
  try:
     downloaded_file_name = await event.client.download_media(reply_msg, './')
  except Exception as e: 
     await event.reply(str(e))
  
  img = Image.open(downloaded_file_name)
  width, height = img.size
  aspect_ratio = height/width
  new_width = 120
  new_height = aspect_ratio * new_width * 0.55
  img = img.resize((new_width, int(new_height)))
  img = img.convert('L')
  pixels = img.getdata()
  chars = ["B","S","#","&","@","$","%","*","!",":","."]
  new_pixels = [chars[pixel//25] for pixel in pixels]
  new_pixels = ''.join(new_pixels)
  new_pixels_count = len(new_pixels)
  ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
  ascii_image = "\n".join(ascii_image)
  with open("ascii.html", "w") as f:
     f.write(ascii_image)
  await event.client.send_file(event.chat_id, f, caption="HERE IS YOUR ASCII ART", reply_to=event.id)
  os.remove(f)



