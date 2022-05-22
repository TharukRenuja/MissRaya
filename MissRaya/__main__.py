from MissRaya.plugins import cmds, cback
from pyrogram import idle
from MissRaya import tbot, pbot
from MissRaya.vars import *
from os import listdir
from os.path import isfile, join
import importlib

mypath = 'MissRaya/plugins'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
Files = []
for file in onlyfiles:
	if file.split('.')[-1] == 'py':
		Files.append(file)
	else:
		pass
Imported = []
for file in Files:
    Imported.append(importlib.import_module(
    	'MissRaya.plugins.{}'.format(file.split('.')[0])))

pbot.start()
tbot.start(bot_token=BOT_TOKEN)
print(BOT_STARTED)
idle()