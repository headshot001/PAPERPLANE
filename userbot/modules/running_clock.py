# Made by @AyushChatterjee, simple and easy code

import asyncio
import datetime
import time
from telethon import events
from userbot import bot, CMD_HELP
from userbot.events import register
import pytz
import pyfiglet


@register(outgoing=True, pattern="^.runclock$", disable_edited=True)
async def _(event):
    if event.fwd_from:
        return
    while True:
        LT = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        OT = LT.strftime("%H:%M:%S")
        input = pyfiglet.figlet_format(OT, font = "small")
        final = f"`{input}`"
        await event.edit(final)
        await asyncio.sleep(1)

CMD_HELP.update({
".runclock":
"Module to show running clock in telegram"
})
