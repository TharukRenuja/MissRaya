from pyrogram import filters
from MissRaya.vars import *
from MissRaya.helpers.funcs import *
from MissRaya import tbot, pbot
from pyrogram.types import InlineQuery, InputMediaPhoto, InlineQueryResultPhoto, InlineQueryResultArticle, InlineKeyboardButton, InlineKeyboardMarkup, InputTextMessageContent
from pyrogram.errors import QueryIdInvalid
from art import *

@pbot.on_inline_query()
async def Inline_Search(_, query: InlineQuery):
	t = query.query.lower()
	results = []
	offset = int(query.offset or 0)
	results.append(InlineQueryResultArticle(
			title=INLINE_ABOUT_TITLE,
			description=INLINE_ABOUT_DES,
			input_message_content=InputTextMessageContent(INLINE_ABOUT_MSG),
			thumb_url=INLINE_ABOUT_THUMB,
			reply_markup=INLINE_ABOUT_BTNS,
		))
	if t == 'help' or t == '!h':
		pass
	elif t == 'about' or 't' == '!a':
		pass
	try:
		await query.answer(results=results[:20], cache_time=5)
	except QueryIdInvalid:
		pass
	except:
		error = traceback.format_exc()
		await SendLog(error, query.from_user.first_name, query.from_user.id, query.from_user.id)

