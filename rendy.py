# made by rendy
import os
from pyrogram import Client, filters
from pyrogram InlineKeyBoardMarkup, InlineKeyBoardButton

bot = Client(
  "test bot"
  bot_token = os.enverion.get("BOT_TOKEN"),
  api_id = int(os.enverion.get("API_ID")),
  api_hash = os.enverion.get("API_HASH),
                             
@Bot.on_message(filters, private & private.all)
async def text(bot, update):
   
  text = "join channel && join groups"
  reply_markup = InlineKeyBoardMarkup(
      [
        [InlineKeyBoardButton(text="join channel", url="https://t.me/RendyProjects)],
        [InlineKeyBoardButton(text="join groups", url="https://t.me/HomeSupport)]
      ]
                              
   )
   
   await update.reply_text(
       text=text,
       reply_markup=reply_markup,
       disable_web_page_preivew=False
       quote=True
   )
         
Bot.run()         
