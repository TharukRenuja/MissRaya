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
  ___      _     ___ _            _          _ 
 | _ ) ___| |_  / __| |_ __ _ _ _| |_ ___ __| |
 | _ \/ _ \  _| \__ \  _/ _` | '_|  _/ -_) _` |
 |___/\___/\__| |___/\__\__,_|_|  \__\___\__,_|
				O_O Miss Raya Bot v1.0.2
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
WELCOME_TEXT = os.environ.get("WELCOME_TEXT", "Hey There, Welcome!")
RULES_TXT = os.environ.get("RULES_TXT", "No Rules. Use Me Freely🤗.")

# Inline About
INLINE_ABOUT_TITLE = os.environ.get("INLINE_ABOUT_TITLE", "🌷 Miss Raya 🌹")
INLINE_ABOUT_THUMB = os.environ.get("INLINE_ABOUT_THUMB", "https://telegra.ph/file/c34ea5555a31864d1dd8d.jpg")
INLINE_ABOUT_DES = os.environ.get("INLINE_ABOUT_DES", "A Simple Group Managing Bot...")
INLINE_ABOUT_MSG = os.environ.get("INLINE_ABOUT_MSG", "<b><u>✨ A Project Of Team SL Bots ⚡</u></b>\n\n🌹 So, You Can Use This Bot Freely...🍁 & Also Please Be Kind Share This Bot With Others If it\'s Not Bad...\n\n💖 If You Have Any Questions... Please Contact Us🤗...🌺")
INLINE_ABOUT_BTNS = InlineKeyboardMarkup([
		[InlineKeyboardButton('⚡ Tharuk Renuja ⚡', url='https://t.me/TharukRenuja'),
		 InlineKeyboardButton('🌷 Senith Chandul 🌷', url='https://t.me/SenithChandul')],
		[InlineKeyboardButton('🤞 Team SL Bots 🤞',
		                      url='https://t.me/SLBotOfficial')],
		[InlineKeyboardButton('🍁 Support 🍁',
		                      url='https://t.me/SLBotsChat')],
		[InlineKeyboardButton('🍀 Inline Again 🍀',
		                      switch_inline_query_current_chat='')]
	])


# About Message
ABOUT_MSG = os.environ.get("ABOUT_MSG", "<b><u>✨ A Project Of Team SL Bots ⚡</u></b>\n\n🌹 So, You Can Use This Bot Freely...🍁 & Also Please Be Kind Share This Bot With Others If it\'s Not Bad...\n\n💖 If You Have Any Questions... Please Contact Us🤗...🌺")
ABOUT_BTNS = InlineKeyboardMarkup([
		[InlineKeyboardButton('⚡ Tharuk Renuja ⚡', url='https://t.me/TharukRenuja'),
		 InlineKeyboardButton('🌷 Senith Chandul 🌷', url='https://t.me/SenithChandul')],
		[InlineKeyboardButton('🤞 Team SL Bots 🤞',
		                      url='https://t.me/SLBotOfficial')],
		[InlineKeyboardButton('🍁 Support 🍁',
		                      url='https://t.me/SLBotsChat')],
		[InlineKeyboardButton('💠 Help', callback_data='help'),
		 InlineKeyboardButton('Close ✖️', callback_data='close')]
	])



