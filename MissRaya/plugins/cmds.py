from pyrogram import filters
from telethon import events
from MissRaya.vars import *
from MissRaya.plugins.help import *
from MissRaya.helpers.funcs import *
from MissRaya import tbot, pbot
from telethon import events, Button

@pbot.on_message(filters.command(commands=['start']))
async def StartMsg(_, m):
	if len(m.text) > 7:
		ty = m.text.split(' ')[-1]
		if ty == 'help':
			return await pbot.send_message(m.chat.id, text=HELP_TEXT, reply_markup=btn)
		elif ty == 'about':
			return await pbot.send_message(m.chat.id, text=ABOUT_MSG, reply_markup=ABOUT_MSG)
		else:
			pass
	await pbot.send_sticker(m.chat.id, sticker='CAACAgUAAxkBAAEEx6ZiiOVbPG7LEPrT7AABBCdfTn9f3n0AAkEEAAJRSklUk7MNzCSLNuIkBA')
	await pbot.send_message(m.chat.id, text=START_MSG.format(m.from_user.mention), reply_markup=START_BTNS)
	if m.chat.type == 'private':
		await AddNewUser(str(m.from_user.username), int(m.from_user.id))

@pbot.on_message(filters.command(commands=['about']))
async def AboutMsg(_, m):
	await pbot.send_message(m.chat.id, text=ABOUT_MSG, reply_markup=ABOUT_BTNS)

@tbot.on(events.NewMessage(pattern="^[/]start$" & "^[/]alive$"))
async def startgrp(event):

    if event.is_group:
       await event.reply("**I am alive!**")
       return