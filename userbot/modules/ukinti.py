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
from userbot.events import register

KICK_RIGHTS = ChatBannedRights(until_date=None, view_messages=True)


@register(pattern=".kickthefools")
async def _(event):
    if event.fwd_from:
        return
    if event.is_private:
        return
    chat = await event.get_chat()
    if not (chat.admin_rights or chat.creator):
       await event.reply("`I am not admin here!`")
       return 
    c = 0
    m = 0
    n = 0
    y = 0
    w = 0   
    await event.reply("Searching Participant Lists...")
    async for i in event.client.iter_participants(event.chat_id):

        if isinstance(i.status, UserStatusLastMonth):
            m = m + 1
            status = await event.client(EditBannedRequest(event.chat_id, i, KICK_RIGHTS))
            if not status:
                    try:
                        await event.reply("I need admin priveleges to perform this action!")
                    except:
                        pass
            else:
               c = c + 1
                    
        if isinstance(i.status, UserStatusLastWeek):
            w = w + 1
            status = await event.client(EditBannedRequest(event.chat_id, i, KICK_RIGHTS))
            if not status:
                    try:
                        await event.reply("I need admin priveleges to perform this action!")
                    except:
                        pass                    
            else:
               c = c + 1

    required_string = "Successfully Kicked **{}** users"
    await event.reply(required_string.format(c))
