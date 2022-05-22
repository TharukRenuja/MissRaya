from pyrogram import filters
from telethon import events
from MissRaya.vars import *
from MissRaya.helpers.funcs import *
from MissRaya import tbot

@tbot.on(events.ChatAction)
async def AddedMe(event):
	try:
		if not event.user_added:
			return
		user = await event.get_user()
		chat = await event.get_chat()
		if not user.is_self:
			return
		if hasattr(chat, 'username'):
			mention = f"[{chat.title}](https://t.me/{chat.username}/{event.action_message.id})"
		else:
			mention = f"[{chat.title}](https://t.me/c/{chat.id}/{event.action_message.id})"
		await AddNewGroup(str(chat.title), int(chat.id), mention=mention)
	except Exception as Error:
		await SendLog(Error, 'None', 'None', chat.id)