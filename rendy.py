# made by rendy

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telethon import Button
from telethon import TelegramClient, events

logging.basicConfig(
    level=logging.INFO
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)



Bot = Client(
    "Join-Channel-Bot",
    bot_token = os.environ.get("BOT_TOKEN"),
    api_id = int(os.environ.get("API_ID")),
    api_hash = os.environ.get("API_HASH")
)


@client.on(events.NewMessage(pattern="^/test ?(.*)")) 
async def test(event):
   await event.reply("hello gay")


@Bot.on_message(filters.private & filters.all)
async def text(bot, update):
    
    text = "join channel & join support groups.\n\nMade by @CuteInspire"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="join channel", url="https://t.me/RendyProjects")],
            [InlineKeyboardButton(text="Join Support", url="https://t.me/HomeSupport")]
        ]
    )
    
    await update.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
         
Bot.run()         
