from telethon import events, Button
from MissRaya import tbot
from MissRaya.vars import *

btn =[
    [Button.inline("Admin", data="gadmin"), Button.inline("Bans", data="ban")],
    [Button.inline("Clean", data="clean"), Button.inline("Pugres", data="purges")],
    [Button.inline("Locks", data="locks"), Button.inline("Misc", data="misc")],
    [Button.inline("Pins", data="pins")],
    [Button.inline('Close', data='close')]]

HELP_TEXT = """
**Hey There! Here's my help menu🤗**

/start - To Start Me ✌
/help - To Get Available Help Menu
/about - To Know About Me & Devs

Powered By **[Team SL Bots](https://t.me/SLBotOfficial)**
"""


@tbot.on(events.NewMessage(pattern="[/]help"))
async def help(event):

    if event.is_group:
       await event.reply("Contact me in PM to get available help menu!", buttons=[
       [Button.url("Help And Commands!", "t.me/{}?start=help".format(BOT_USERNAME))]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@tbot.on(events.NewMessage(pattern="^/start help"))
async def _(event):

    await event.reply(HELP_TEXT, buttons=btn)

@tbot.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):

     await event.edit(HELP_TEXT, buttons=btn)
