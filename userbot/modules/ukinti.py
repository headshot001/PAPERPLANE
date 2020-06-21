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
  
    chat = await event.get_chat()
   
    if not chat.admin_rights or chat.creator:
        await event.reply("NO_ADMIN")
        return
    
    c = 0
    KICK_RIGHTS = ChatBannedRights(until_date=None, view_messages=True)
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

        if isinstance(i.status, UserStatusLastMonth):
            status = await event.client(EditBannedRequest(event.chat_id, i, KICK_RIGHTS))
            if not status:
               return
            else:
               c = c + 1
    
    required_string = "Successfully Kicked **{}** users"
    await event.reply(required_string.format(c))

async def get_user_from_id(user, event):
    """ Getting user from user ID """
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None

    return user_obj

import cv2
import numpy as np
import mapper
import os

@register(pattern="^/camscanner")
async def asciiart(event):
  if event.fwd_from:
     return  
  if not event.from_id:
     await event.reply("Reply To A Image Plox..")
     return
  reply_msg = await event.get_reply_message()
  downloaded_file_name = await event.client.download_media(reply_msg, './')

  image=cv2.imread(downloaded_file_name)   #read in the image
  image=cv2.resize(image,(1300,800)) #resizing because opencv does not work well with bigger images
  orig=image.copy()
  gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  #RGB To Gray Scale
  cv2.imshow("Title",gray)

  blurred=cv2.GaussianBlur(gray,(5,5),0)  #(5,5) is the kernel size and 0 is sigma that determines the amount of blur
  cv2.imshow("Blur",blurred)

  edged=cv2.Canny(blurred,30,50)  #30 MinThreshold and 50 is the MaxThreshold
  cv2.imshow("Canny",edged)

  contours,hierarchy=cv2.findContours(edged,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  #retrieve the contours as a list, with simple apprximation model
  contours=sorted(contours,key=cv2.contourArea,reverse=True)

  for c in contours:
    p=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.02*p,True)

    if len(approx)==4:
        target=approx
        break
  approx=mapper.mapp(target) #find endpoints of the sheet

  pts=np.float32([[0,0],[800,0],[800,800],[0,800]])  #map to 800*800 target window

  op=cv2.getPerspectiveTransform(approx,pts)  #get the top or bird eye view effect
  dst=cv2.warpPerspective(orig,op,(800,800))

  cv2.imwrite("./scanned.pdf", dst)

  omg = await event.client.upload_file('./scanned.pdf')

  await event.client.send_file(event.chat_id, omg)
  os.remove("./scanned.pdf")
