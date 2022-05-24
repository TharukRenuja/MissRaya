import os
from telethon import Button
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Main Details
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
INLINE_THUMB = os.environ.get("INLINE_THUMB", "https://telegra.ph/file/c34ea5555a31864d1dd8d.jpg")
BOT_STARTED = '''
 
   __  _______________  ___  _____  _____ 
  /  |/  /  _/ __/ __/ / _ \/ _ \ \/ / _ |
 / /|_/ // /_\ \_\ \  / , _/ __ |\  / __ |
/_/  /_/___/___/___/ /_/|_/_/ |_|/_/_/ |_|
                                           
 
 ___      _     ___ _            _          _ 
 | _ ) ___| |_  / __| |_ __ _ _ _| |_ ___ __| |
 | _ \/ _ \  _| \__ \  _/ _` | '_|  _/ -_) _` |
 |___/\___/\__| |___/\__\__,_|_|  \__\___\__,_|
				O_O Miss Raya Bot v1.0
				Powered By Pyrogram & Telethon
				Using Firebase as a Database
				Developed By Team SL Bots </>  
'''
LOG_CHNL = os.environ.get("LOG_CHNL", "-1001759089181")
FDBURL = os.environ.get("FDBURL")
# Start Message
START_MSG = os.environ.get("START_MSG", "🌷 Hi There {}🔥,\n**I am Miss Raya🌹...**")
START_BTNS = InlineKeyboardMarkup([
		[InlineKeyboardButton('🌹 Help', callback_data='help'),
		 InlineKeyboardButton('About 🌷', callback_data='about')],
		[InlineKeyboardButton("➕ Add Miss Raya to Your Group ➕", url="t.me/MissRayaBot?startgroup=true")]
	])


# Inline About
INLINE_ABOUT_TITLE = os.environ.get("API_ID", "🌷 Miss Raya 🌹")
INLINE_ABOUT_THUMB = 'https://telegra.ph/file/c34ea5555a31864d1dd8d.jpg'
INLINE_ABOUT_DES = 'A Simple Group Managing Bot'
INLINE_ABOUT_MSG = '<b><u>🌻 Ⲇ Ⲣⲅⲟⳗⲉⲥⲧ Ⲟ⳨ ⲊⳐ Ⲃⲟⲧ⳽ 🌻</u></b>\n\n🌴 Tʜɪs Bᴏᴛ Wᴀs Cᴏᴅᴇᴅ Aɴᴅ Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ Ⲧⲏⲇⲅⳙⲕ Ⲅⲉⲛⳙⳗⲇ Aɴᴅ Ⲋⲉⲛⲓⲧⲏ Ⲥⲏⲇⲛ𝖽ⳙⳑ... 🌷\n\n🌹 Sᴏ, Yᴏᴜ Cᴀɴ Usᴇ Tʜɪs Bᴏᴛ Fʀᴇᴇʟʏ...🍁 Aɴᴅ Aʟsᴏ Pʟᴇᴀsᴇ Bᴇ Kɪɴᴅ Sʜᴀʀᴇ Tʜɪs Bᴏᴛ Wɪᴛʜ Oᴛʜᴇʀ Iꜰ Iᴛ\'s Nᴏᴛ Bᴀᴅ...\n\n💐 Aʟsᴏ Yᴏᴜ Cᴀɴ Cᴏɴᴛᴀᴄᴛ Us Fʀᴏᴍ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴs... Iꜰ Yᴏᴜ Hᴀᴠᴇ Aɴʏ Qᴜᴇsᴛɪᴏɴ... Pʟᴇᴀsᴇ Cᴏɴᴛᴀᴄᴛ Us...🌺'
INLINE_ABOUT_BTNS = InlineKeyboardMarkup([
		[InlineKeyboardButton('🌻 Ⲧⲏⲇⲅⳙⲕ Ⲅⲇⲛⳙⳗⲇ 🌻', url='https://t.me/ImTharuk'),
		 InlineKeyboardButton('🌷 Ⲋⲉⲛⲓⲧⲏ Ⲥⲏⲇⲛ𝖽ⳙⳑ 🌷', url='https://t.me/SenithChandul')],
		[InlineKeyboardButton('🌹 ⲊⳐ Ⲃⲟⲧ⳽ Ⲟ⳨⳨ⲓⲥⲓⲇⳑ 🌹',
		                      url='https://t.me/SLBotOfficial')],
		[InlineKeyboardButton('🍁 Support 🍁',
		                      url='https://t.me/trtechguide')],
		[InlineKeyboardButton('🍀 Iɴʟɪɴᴇ Aɢᴀɪɴ 🍀',
		                      switch_inline_query_current_chat='')]
	])


# About Message
ABOUT_MSG = '<b><u>🌻 Ⲇ Ⲣⲅⲟⳗⲉⲥⲧ Ⲟ⳨ ⲊⳐ Ⲃⲟⲧ⳽ 🌻</u></b>\n\n🌴 Tʜɪs Bᴏᴛ Wᴀs Cᴏᴅᴇᴅ Aɴᴅ Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ Ⲧⲏⲇⲅⳙⲕ Ⲅⲉⲛⳙⳗⲇ Aɴᴅ Ⲋⲉⲛⲓⲧⲏ Ⲥⲏⲇⲛ𝖽ⳙⳑ... 🌷\n\n🌹 Sᴏ, Yᴏᴜ Cᴀɴ Usᴇ Tʜɪs Bᴏᴛ Fʀᴇᴇʟʏ...🍁 Aɴᴅ Aʟsᴏ Pʟᴇᴀsᴇ Bᴇ Kɪɴᴅ Sʜᴀʀᴇ Tʜɪs Bᴏᴛ Wɪᴛʜ Oᴛʜᴇʀ Iꜰ Iᴛ\'s Nᴏᴛ Bᴀᴅ...\n\n💐 Aʟsᴏ Yᴏᴜ Cᴀɴ Cᴏɴᴛᴀᴄᴛ Us Fʀᴏᴍ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴs... Iꜰ Yᴏᴜ Hᴀᴠᴇ Aɴʏ Qᴜᴇsᴛɪᴏɴ... Pʟᴇᴀsᴇ Cᴏɴᴛᴀᴄᴛ Us...🌺'
ABOUT_BTNS = InlineKeyboardMarkup([
		[InlineKeyboardButton('🌻 Ⲧⲏⲇⲅⳙⲕ Ⲅⲇⲛⳙⳗⲇ 🌻', url='https://t.me/ImTharuk'),
		 InlineKeyboardButton('🌷 Ⲋⲉⲛⲓⲧⲏ Ⲥⲏⲇⲛ𝖽ⳙⳑ 🌷', url='https://t.me/SenithChandul')],
		[InlineKeyboardButton('🌹 ⲊⳐ Ⲃⲟⲧ⳽ Ⲟ⳨⳨ⲓⲥⲓⲇⳑ 🌹',
		                      url='https://t.me/SLBotOfficial')],
		[InlineKeyboardButton('🍁 Support 🍁',
		                      url='https://t.me/trtechguide')],
		[InlineKeyboardButton('🌹 Hᴇʟᴘ', callback_data='help'),
		 InlineKeyboardButton('Cʟᴏsᴇ ✖️', callback_data='close')]
	])

# Help Message
HELP_MSG = "Help"
HELP_BTNS = InlineKeyboardMarkup([
    [InlineKeyboardButton('🌷 Aʙᴏᴜᴛ', callback_data='about'),
     InlineKeyboardButton('Iɴʟɪɴᴇ Mᴇɴᴜ 💐', callback_data='inline'),
	 InlineKeyboardButton('🍀 Iɴʟɪɴᴇ Hᴇʀᴇ', switch_inline_query_current_chat='')],
  		[InlineKeyboardButton('🔙 Bᴀᴄᴋ ', callback_data='start'),
     InlineKeyboardButton('Cʟᴏsᴇ ✖️', callback_data='close')]
	])



