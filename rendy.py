# made by rendy

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Join-Channel-Bot",
    bot_token = os.environ.get("BOT_TOKEN"),
    api_id = int(os.environ.get("API_ID")),
    api_hash = os.environ.get("API_HASH")
)


@Bot.on_message(filters.private & filters.all)
async def text(bot, update):
    
    text = "join channel & join groups.\n\nMade by @CuteInspire"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="join channel", url="https://t.me/RendyProjects")],
            [InlineKeyboardButton(text="Search in another chat", url="https://t.me/HomeSupport")]
        ]
    )
    
    await update.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
         
Bot.run()         
