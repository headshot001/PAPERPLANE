# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
#

"""
Copyright (C) 2019 The Raphielscape Company LLC.

Genius lyrics plugin
	get this value from https://genius.com/developers

Lyrics Plugin Syntax:
	.lyrics <aritst name, song nane>
"""

from userbot.events import register
import os
from telethon.tl.types import DocumentAttributeFilename, MessageMediaPhoto
from telethon import events
from userbot import GENIUS_API, CMD_HELP


"""Genius(lyrics) staff"""
GApi = GENIUS_API
import lyricsgenius
genius = lyricsgenius.Genius(GApi)


@register(outgoing=True, pattern="^.lyrics (.*)")
async def lyrics(lyr):
	if GApi == "None":
		await lyr.edit("`please provide genius api token to config.py or Heroku Var first`")
	try:
		args = lyr.text.split()
		artist = lyr.text.split()[1]
		snameinit = lyr.text.split(' ', 2)
		sname = snameinit[2]
	except Exception:
		await lyr.edit("`Lel pls provide artist and song names U Dumb`")
		return

	#Try to search for * in artist string(for multiword artist name)
	try:
		artist = artist.replace('*', ' ')
	except Exception:
		artist = lyr.text.split()[1]
		pass

	if len(args) < 3:
		await lyr.edit("`Please provide artist and song names`")

	await lyr.edit(f"`Searching lyrics for {artist} - {sname}...`")

	try:
		song = genius.search_song(sname, artist)
	except TypeError:
		song = None

	if song is None:
		await lyr.edit(f"Song **{artist} - {sname}** not found!")
		return
	if len(song.lyrics) > 4096:
			await lyr.edit("`Lyrics is too big, view the file to see it.`")
			file = open("lyrics.txt", "w+")
			file.write(f"Search query: \n{artist} - {sname}\n\n{song.lyrics}")
			file.close()
			await lyr.client.send_file(
				lyr.chat_id,
				"lyrics.txt",
				reply_to=lyr.id,
			)
			os.remove("lyrics.txt")
	else:
		await lyr.edit(f"**Search query**: \n`{artist} - {sname}`\n\n```{song.lyrics}```")
	return

CMD_HELP.update({
"lyrics"
"Module to search for song lyrics/nPATTERN : `.song singer(optional) songname`
})
