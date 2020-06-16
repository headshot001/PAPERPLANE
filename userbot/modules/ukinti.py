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
  downloaded_file_name = await event.client.download_media(reply_msg, './')
  os.system(f'python3 ascii {downloaded_file_name}')
  omg = await event.client.upload_file('./ascii.html')
  await event.client.send_file(event.chat_id, omg)
