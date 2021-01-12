from bot.bot import Bot
from bot.handler import MessageHandler
from config import TOKEN
from config import myteam_api_url

bot = Bot(token=TOKEN, api_url_base=myteam_api_url)

def message_cb(bot, event):
    bot.send_text(chat_id=event.from_chat, text=event.text)

bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
bot.start_polling()
bot.idle()
