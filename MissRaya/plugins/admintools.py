from pyrogram import filters
from telethon import events
from MissRaya.vars import *
from MissRaya.helpers.funcs import *
from MissRaya import tbot, pbot

@tbot.on(events.NewMessage(pattern='/.*promote'))
async def Promote(event):
	sender = await event.get_sender()
	chat = await event.get_chat()
	try:
		if IsAdmin(sender.id):
			message = event.message
			text = message.message
			if len(text) == 8:
				reply = await event.get_reply_message()
				r_sender = reply.sender
				UserName, ID = r_sender.username, r_sender.id
			else:
				UserName, ID = text[9:].split(' ')
			await AddNewAdmin(str(UserName), int(ID))
			await tbot.send_message(chat, '🌺 Promoted User {} As Admin... 🌷'.format('@{}'.format(UserName) if UserName != None else ID))
		else:
			pass
	except Exception as Error:
		sender = await event.get_sender()
		await SendLog(Error, sender.first_name, sender.id, chat.id)


@tbot.on(events.NewMessage(pattern='/.*broadcast'))
async def broadcast(e):
	c, s, r = await e.get_chat(), await e.get_sender(), await e.get_reply_message()
	if IsAdmin(s.id):
		await ALLCast(c.id, r.id, s.first_name, s.id)

@tbot.on(events.NewMessage(pattern='/.*count', from_users=GetAdminIdList()))
async def SendUserList(e):
	c = await e.get_chat()
	await ProcessingMsg(c.id, 0.5)
	Groups = GetGrps()
	Users = GetUsers()
	Data = '<b><u>🌷 Hᴇʀᴇ Is Dᴇᴛᴀɪʟs Oꜰ Usᴇʀs Aɴᴅ Gʀᴏᴜᴘs Iɴ Dᴀᴛᴀʙᴀsᴇ...🌹</u></b>\n\n<b>Usᴇʀs:</b> <code>{}</code>\n<b>Gʀᴏᴜᴘs:</b> <code>{}</code>\n<b>Aʟʟ:</b> <code>{}</code>'.format(
		len(Users), len(Groups), len(Users)+len(Groups))
	await tbot.send_message(c, Data, buttons=[[Button.inline('🌺 Gᴇɴᴇʀᴀᴛᴇ Lɪsᴛ 💐', data='genuserlist')]], parse_mode='html')
