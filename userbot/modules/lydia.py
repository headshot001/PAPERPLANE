from coffeehouse.lydia import LydiaAI
from coffeehouse.api import API
import asyncio
from userbot import LYDIA_API_KEY
from userbot import BOTLOG, CMD_HELP, bot
from userbot.events import register

ACC_LYDIA = {}
if LYDIA_API_KEY:
    api_key = LYDIA_API_KEY
    api_client = API(api_key)
    lydia = LydiaAI(api_client)

@register(outgoing=True, disable_errors=True, pattern="^.autochat$")
async def addcf(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    await event.edit("Running...")
    await asyncio.sleep(4)
    await event.edit("Still Running....")
    reply_msg = await event.get_reply_message()
    if reply_msg:
        session = lydia.create_session()
        session_id = session.id
        if reply_msg.from_id is None:
            return await event.edit("Invalid user type.")
        ACC_LYDIA.update({(event.chat_id & reply_msg.from_id): session})
        await event.edit("Auto reply activated for user: {} in chat: {}".format(str(reply_msg.from_id), str(event.chat_id)))
    else:
        await event.edit("Tag any user's message to activate on them")

@register(outgoing=True, disable_errors=True, pattern="^.stopchat$")
async def remcf(event):
    if event.fwd_from:
        return
    await event.edit("Running..")
    await asyncio.sleep(4)
    await event.edit("Processing...")
    reply_msg = await event.get_reply_message()
    try:
        del ACC_LYDIA[event.chat_id & reply_msg.from_id]
        await event.edit(" Auto reply disabled for user: {} in chat: {}".format(str(reply_msg.from_id), str(event.chat_id)))
    except Exception:
        await event.edit("This person does not have activated auto reply on him/her.")

@register(incoming=True, disable_errors=True, disable_edited=True)
async def user(event):
    user_text = event.text
    try:
        session = ACC_LYDIA[event.chat_id & event.from_id]
        msg = event.text
        async with event.client.action(event.chat_id, "typing"):
            text_rep = session.think_thought(msg)
            wait_time = 0
            for i in range(len(text_rep)):
                wait_time = wait_time + 0.1
            await asyncio.sleep(wait_time)
            await event.reply(text_rep)
    except (KeyError, TypeError):
        return

CMD_HELP.update({
"autochat":
"use .autochat command in reply to someone's text to randomly talk to them like a bot"
})
