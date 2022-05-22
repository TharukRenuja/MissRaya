from distutils.command.config import config
import traceback, os, io, re, asyncio
from telethon import events, Button
from pyrogram.errors import InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from MissRaya import tbot, pbot
from .db import *
from art import *
from MissRaya.vars import *

LogChannel = LOG_CHNL

def IsAdmin(id):
    Admins = GetAdmins()
    for admin in Admins:
        if int(admin) == id:
            isAdmin = True
            break
        else:
            isAdmin = False
    return isAdmin


def IsCommand(text):
    try:
        if text == None:
            return False
        elif text[0] == '/':
            return True
        else:
            return False
    except:
        return False



async def AddNewUser(UserName: str, ID: int):
    Added = GetUsers()
    IsAdded = False
    for key in Added:
        if int(key) == ID:
            IsAdded = True
            break
        else:
            pass
    if IsAdded == False:
        AddUser(UserName, ID)
        msg = '💥 Nᴇᴡ Usᴇʀ 💥\n🌴 UsᴇʀNᴀᴍᴇ : {}\n🌴 ID : {}\n🌴 Aʟʟ Usᴇʀs : {}'.format(
            '@{}'.format(UserName) if UserName != None else 'None', ID, len(Added))
        await tbot.send_message(LogChannel, msg)


async def AddNewGroup(Title: str, ID: int, mention):
    Added = GetGrps()
    IsAdded = False
    for key in Added:
        if int(key) == ID:
            IsAdded = True
        else:
            pass
    if IsAdded == False:
        AddGroup(Title, ID)
        await tbot.send_message(LogChannel, f'💥 Nᴇᴡ Gʀᴏᴜᴘ 💥\n🌴 UsᴇʀNᴀᴍᴇ : {Title}\n🌴 ID : {ID}\n🌴 Aʟʟ Gʀᴏᴜᴘs : {len(Added)}')


async def AddNewAdmin(UserName: str, ID: int):
    Added = GetAdmins()
    IsAdded = False
    for key in Added:
        if int(key) == ID:
            IsAdded = True
        else:
            pass
    if IsAdded == False:
        AddAdmin(UserName, ID)
        msg = '💥 Nᴇᴡ Aᴅᴍɪɴ 💥\n🌴 UsᴇʀNᴀᴍᴇ : {}\n🌴 ID : {}\n🌴 Aʟʟ Aᴅᴍɪɴs : {}'.format('@{}'.format(UserName) if UserName != None else 'None', ID, len(Added))
        await tbot.send_message(LogChannel, msg)

async def ALLCast(from_chat_id, message_id, first_name, sender_id, forward=False):
    Groups = GetGrps()
    Users = GetUsers()
    await pbot.send_message(from_chat_id, f'🌴 BROΔDCΔSΓ SΓΔRΓED...! 🌹\n🌾 Sending This Post To **{len(Users)}** Users....🌻\n🌾 Sending This Post To **{len(Groups)}** Groups....🌻')
    SentGrp = 0
    SentUsr = 0
    for key in Users:
        try:
            if forward:
                await pbot.forward_messages(chat_id=int(key), from_chat_id=from_chat_id, message_ids=message_id)
            else:
                await pbot.copy_message(chat_id=int(key), from_chat_id=from_chat_id, message_id=message_id)
            SentUsr += 1
        except InputUserDeactivated:
            RemUser(int(key))
        except UserIsBlocked:
            RemUser(int(key))
        except PeerIdInvalid:
            RemUser(int(key))
        except Exception:
            await SendLog(traceback.format_exc(), first_name, sender_id, from_chat_id)
    for key in Groups:
        try:
            if forward:
                await pbot.forward_messages(chat_id=int(key), from_chat_id=from_chat_id, message_ids=message_id)
            else:
                await pbot.copy_message(chat_id=int(key), from_chat_id=from_chat_id, message_id=message_id)
            SentGrp += 1
        except InputUserDeactivated:
            RemUser(int(key))
        except UserIsBlocked:
            RemUser(int(key))
        except PeerIdInvalid:
            RemUser(int(key))
        except Exception:
            pass
    await pbot.send_message(from_chat_id, f'🌻 𝔖𝔢𝔫𝔡𝔦𝔫𝔤 𝔬𝔣 𝔱𝔥𝔢 𝔟𝔯𝔬𝔞𝔡𝔠𝔞𝔰𝔱 𝔭𝔬𝔰𝔱 𝔦𝔰 𝔰𝔲𝔠𝔠𝔢𝔰𝔰𝔣𝔲𝔩𝔩𝔶 𝔠𝔬𝔪𝔭𝔩𝔢𝔱𝔢𝔡! 🌺\nSent To ⚡️ {SentUsr} ⚡️ Users....🌷\nSent To ⚡️ {SentGrp} ⚡️ Users....🌷')


async def SendLog(log, fname, id, chat):
    await tbot.send_message(LogChannel, f'🌷 Bot Crashed 🍇\n\nTo User ⚡️ [{fname}](tg://user?id={id})\nIn Chat ⚡️ `{chat}`\nError Log 🌴```{log}```')



def GetAdminIdList():
    Admins = GetAdmins()
    IDs = []
    for key in Admins:
        IDs.append(int(key))
    return IDs

async def ProcessingMsg(chat_id, time, delete=True):
    txt = ['Pʀᴏᴄᴇssɪɴɢ [ 🌼 ]', 'Pʀᴏᴄᴇssɪɴɢ [ 🌼 🌼 ]', 'Pʀᴏᴄᴇssɪɴɢ [ 🌼 🌼 🌼 ]']
    m = await tbot.send_message(chat_id, txt[0])
    time_one = round(time/3, 3)
    for x in range(1, 3):
        await asyncio.sleep(time_one)
        await tbot.edit_message(chat_id, m, txt[x])
    if delete:
        await asyncio.sleep(time_one)
        await tbot.delete_messages(chat_id, m)
    else:
        return m


async def GetUsrsGrpsToTxt(chat):
    Users = GetUsers()
    Groups = GetGrps()
    FileName = 'UsrsAndGrps.txt'
    Data = 'Here Is A List Of Users In Database...\n\n'    
    for key, val in Users.items():
        Data = f'{Data}==> @{val}: {key}\n'
    Data = f'{Data}\n-----------------------------------------------------------------'
    Data = f'{Data}\n\nHere Is A List Of Groups In Database...\n\n'
    for key, val in Groups.items():
        Data = f'{Data}==> {val}: {key}\n'
    Data = f'{Data}\n-----------------------------------------------------------------'
    Data = f'{Data}\n\nAll Users: {len(Users)}\nAll Groups: {len(Groups)}'
    with io.open(FileName, 'w', encoding='utf-8') as f:
        f.write(Data)
    await tbot.send_message(chat, file=FileName, message='**🌷 Hᴇʀᴇ Is A Lɪsᴛ Oꜰ Usᴇʀs Iɴ Yᴏᴜʀ Dᴀᴛᴀʙᴀsᴇ 🌻**')
    os.remove(FileName)

def GetButtonText(m, d):
    try:
        k = m.reply_markup.inline_keyboard
    except:
        return
    for bs in k:
        for b in bs:
            if b.callback_data == d:
                return b.text
