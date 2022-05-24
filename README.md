# 🌷Miss Raya🌷
A Simple Group Manager Bot using Pyrogram, Telethon. Specially This is working with firebase database.
<p align="middle">
  <img src="https://telegra.ph/file/c34ea5555a31864d1dd8d.jpg" width='400"'>
</p>
<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg">

  </a>
</p>
<p align="center">
  <a href="https://github.com/TharukRenuja/MissRaya/stargazers">
    <img src="https://img.shields.io/github/stars/TharukRenuja/MissRaya?style=social">

  </a>
  
  <a href="https://github.com/TharukRenuja/MissRaya/fork">
    <img src="https://img.shields.io/github/forks/TharukRenuja/MissRaya?label=Fork&style=social">

  </a>  
</p>

## Plugins not included yet ⚠

## Deploy

### Easy Method
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/Y1pXr6?referralCode=ImTharuk) [![Deploy on Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/TharukRenuja/MissRaya)

### Hard Method
```sh
# Install Git First (apt-instll git)
$ git clone https://github.com/TharukRenuja/MissRaya
$ cd MissRaya
# Install All Requirements 
$ pip3 install -r requirements.txt
# Add Your Details to ./MissRaya/vars.py
# Start Bot 
$ python3 -m MissRaya
```
##### Mandatory Vars
```
[+] Make Sure You Add All These Mandatory Vars. 
    [-] API_ID:   You can get this value from my.telegram.org
    [-] API_HASH :   You can get this value from my.telegram.org
    [-] FDBURL : Your Firebase DataBase Url. (You can get this value from console.firebase.google.com)
    [-] BOT_TOKEN: Get from @BotFather
    [-] LOG_CHNL: Your Log Channel ID. (Make sure bot is admin in channel)
    [-] BOT_USERNAME: Bot Username.
[+] The MissRaya won't run without setting the mandatory vars.
```

## Important ⚠

[+] Go to console.firebase.google.com & Go to Your Project & Go to Project Settings & Go to Service Accounts & Click on <b>Generate New Private Key</b> & It will Download your Database Credentials File & Then rename it to Database.json & Put it on main directory on MissRaya. MissRaya won't work if you don't put it correctly.

[+] After you got the database url replace the string on <b><a href="https://github.com/TharukRenuja/MissRaya/blob/264a07ffc9d8c20b1b7c85c83b2f6391dfc2a6af/MissRaya/helpers/db.py#L11"> Here </b></a> into your realtime database url <b>on your forked repository</b>. 

[+] You Must Need To Create Some Keys on Firebase Realtime Database. It's on down below pitcure👇
<p align="center">
  <img src="https://user-images.githubusercontent.com/90763454/169789605-70b386ca-ebe6-4aa2-a2b2-d01b5120f1e5.png"> 
</p>

[+] And then you need to Admins in database as like this👇. You must need at least one admin on bot. You can add new admins through bot after you deployed.
<p align="center">
  <img src="https://user-images.githubusercontent.com/90763454/169789380-d229f6d1-f52c-4033-a930-0dc4d99e0cb5.png"> 
</p>


##### Should any be missing kindly let us know at [Developers](https://t.me/SLBotOfficial) or simply submit a pull request on the readme.

# Contributors
![GitHub Contributors Image](https://contrib.rocks/image?repo=TharukRenuja/MissRaya)

 [![SLBots](https://img.shields.io/badge/SLBotOfficial-Channel-orange?style=style=flat&logo=telegram)](https://telegram.dog/SLBotOfficial)   [![SLBots](https://img.shields.io/badge/SLBotOfficial-Support-red?style=flat&logo=telegram)](https://telegram.dog/trtechguide)  [![SLBots](https://img.shields.io/badge/SLBots-Website-red?style=flat&logo=CodersRank)](https://www.slbots.org)   [![MIT license](https://img.shields.io/badge/License-MIT-blue?style=flat)](https://github.com/TharukRenuja/MissRaya/blob/main/LICENSE)  [![Open Source](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/TharukRenuja/MissRaya)
