import aiohttp
from pyrogram import Client
from MissRaya.vars import *
from telethon import TelegramClient
from pyromod import listen

pbot = Client("MissRaya-Pyrogram", bot_token=BOT_TOKEN,
             api_hash=API_HASH, api_id=API_ID,)
tbot = TelegramClient("MissRaya-Telethon", api_id=API_ID, api_hash=API_HASH)
aiohttpsession = aiohttp.ClientSession()