from pyrogram import filters
from MissRaya.vars import *
from MissRaya.helpers.funcs import *
from MissRaya import tbot, pbot

@pbot.on_callback_query(filters.regex('start'))
async def LoadStart(_, u):
	await u.answer(GetButtonText(u.message, u.data))
	await pbot.edit_message_text(u.message.chat.id, u.message.message_id, text=START_MSG.format(u.from_user.mention), reply_markup=START_BTNS)

@pbot.on_callback_query(filters.regex('about'))
async def LoadAbout(_, u):
	await u.answer(GetButtonText(u.message, u.data))
	await pbot.edit_message_text(u.message.chat.id, u.message.message_id, text=ABOUT_MSG, reply_markup=ABOUT_BTNS)

@pbot.on_callback_query(filters.regex('help'))
async def LoadHelp(_, u):
	await u.answer(GetButtonText(u.message, u.data))
	await pbot.edit_message_text(u.message.chat.id, u.message.message_id, text=HELP_MSG, reply_markup=HELP_BTNS)

@pbot.on_callback_query(filters.regex('close'))
async def CloseMenu(_, u):
	await u.message.delete()

@tbot.on(events.CallbackQuery(data='genuserlist'))
async def UserAndGroupsGen(e):
	c = await e.get_chat()
	m = await e.get_message()
	await GetUsrsGrpsToTxt(c)
	await m.delete()
