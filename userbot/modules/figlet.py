"""use cmd .figlet <YOUR_WORD>"""

import asyncio
import pyfiglet
from telethon import events, functions
from userbot.events import register
import sys
 
@register(outgoing=True, pattern="^.figlet (.*)")
async def figlet(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    result = pyfiglet.figlet_format(input_str)
    await event.respond("`{}`".format(result))
    await event.delete()
      
