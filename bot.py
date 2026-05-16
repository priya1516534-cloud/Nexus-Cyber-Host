import telebot
from config import BOT_TOKEN, CHANNEL_ID

bot = telebot.TeleBot(BOT_TOKEN)

def upload_to_telegram(file_path):
    try:
        with open(file_path, 'rb') as f:
            msg = bot.send_document(CHANNEL_ID, f)
            return msg.document.file_id, msg.message_id
    except Exception as e:
        print(f"Error: {e}")
        return None, None
      
