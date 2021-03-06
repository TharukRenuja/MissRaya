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
START_MSG = os.environ.get("START_MSG", "๐ท Hi There {}๐ฅ,\n**I am Miss Raya๐น...**")
START_BTNS = InlineKeyboardMarkup([
		[InlineKeyboardButton('๐น Help', callback_data='help'),
		 InlineKeyboardButton('About ๐ท', callback_data='about')],
		[InlineKeyboardButton("โ Add Miss Raya to Your Group โ", url="t.me/MissRayaBot?startgroup=true")]
	])
WELCOME_TEXT = os.environ.get("WELCOME_TEXT", "Hey There, Welcome!")
RULES_TXT = os.environ.get("RULES_TXT", "No Rules. Use Me Freely๐ค.")

# Inline About
INLINE_ABOUT_TITLE = os.environ.get("INLINE_ABOUT_TITLE", "๐ท Miss Raya ๐น")
INLINE_ABOUT_THUMB = os.environ.get("INLINE_ABOUT_THUMB", "https://telegra.ph/file/c34ea5555a31864d1dd8d.jpg")
INLINE_ABOUT_DES = os.environ.get("INLINE_ABOUT_DES", "A Simple Group Managing Bot...")
INLINE_ABOUT_MSG = os.environ.get("INLINE_ABOUT_MSG", "<b><u>โจ A Project Of Team SL Bots โก</u></b>\n\n๐น So, You Can Use This Bot Freely...๐ & Also Please Be Kind Share This Bot With Others If it\'s Not Bad...\n\n๐ If You Have Any Questions... Please Contact Us๐ค...๐บ")
INLINE_ABOUT_BTNS = InlineKeyboardMarkup([
		[InlineKeyboardButton('โก Tharuk Renuja โก', url='https://t.me/TharukRenuja'),
		 InlineKeyboardButton('๐ท Senith Chandul ๐ท', url='https://t.me/SenithChandul')],
		[InlineKeyboardButton('๐ค Team SL Bots ๐ค',
		                      url='https://t.me/SLBotOfficial')],
		[InlineKeyboardButton('๐ Support ๐',
		                      url='https://t.me/SLBotsChat')],
		[InlineKeyboardButton('๐ Inline Again ๐',
		                      switch_inline_query_current_chat='')]
	])


# About Message
ABOUT_MSG = os.environ.get("ABOUT_MSG", "<b><u>โจ A Project Of Team SL Bots โก</u></b>\n\n๐น So, You Can Use This Bot Freely...๐ & Also Please Be Kind Share This Bot With Others If it\'s Not Bad...\n\n๐ If You Have Any Questions... Please Contact Us๐ค...๐บ")
ABOUT_BTNS = InlineKeyboardMarkup([
		[InlineKeyboardButton('โก Tharuk Renuja โก', url='https://t.me/TharukRenuja'),
		 InlineKeyboardButton('๐ท Senith Chandul ๐ท', url='https://t.me/SenithChandul')],
		[InlineKeyboardButton('๐ค Team SL Bots ๐ค',
		                      url='https://t.me/SLBotOfficial')],
		[InlineKeyboardButton('๐ Support ๐',
		                      url='https://t.me/SLBotsChat')],
		[InlineKeyboardButton('๐? Help', callback_data='help'),
		 InlineKeyboardButton('Close โ๏ธ', callback_data='close')]
	])



