import Constants as keys
import Response as R
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
import json
import sys
sys.path.append('Method/News')
import News
import time

print("Bot: Start!")

def start_command(update: Update, context: CallbackContext) -> None:
  update.message.reply_text(f'Hi {update.effective_user.last_name}')

def help_command(update: Update, context: CallbackContext):
  update.message.reply_text("What can I help you? \n 1. Read the paper -> /news <amount> \n 2. Stop! --> /end or /exit \n 3. LICENSE --> /license")

def news_command(update: Update, context: CallbackContext):
  try:
    limit_news = int(context.args[0]) # Lấy tham số từ input truyền vào -> cào về bao nhiêu tin
    news = News.GetNews(limit_news)
    for x in range(0, len(news)): # Deserialize dữ liệu json trả về từ file News.py lúc nãy
      message = json.loads(news[x])
      update.message.reply_text(message['title'] + "\n" 
        + message['link'] + "\n" + message['description'])
  except (IndexError, ValueError):
    update.message.reply_text('None!')

def end_command(update: Update, content: CallbackContext):  # exit Function
  print("Bot exit with 0")
  exit(0)

def license_command(update: Update, content: CallbackContext):
  update.message.reply_text("This is open source software, without a license")



def handle_message(update: Update, context: CallbackContext):
  text = str(update.message.text).lower()
  response = R.sample_response(text)
  update.message.reply_text(response)  

 # Hàm báp lỗi
def error(update: Update, context: CallbackContext):
  print(f"Update {update} cause error {context.error}")
  update.message.reply_text(f"Update {update} cause error {context.error}")
  time.sleep(3)
  print("Bot exit with 0")
  update.message.reply_text("Sorry, because there was an unexpected problem, the bot will be temporarily closed.")
  exit(0)
  

def main():
  updater = Updater(keys.API_KEY, use_context=True)
  dp = updater.dispatcher
  dp.add_handler(CommandHandler("start", start_command))
  dp.add_handler(CommandHandler("help", help_command))
  dp.add_handler(CommandHandler("news", news_command))
  dp.add_handler(CommandHandler("end", end_command))
  dp.add_handler(CommandHandler("exit", end_command))
  dp.add_handler(CommandHandler("license", license_command))
  dp.add_handler(MessageHandler(Filters.text, handle_message))
  dp.add_error_handler(error)

  updater.start_polling()
  updater.idle()

main()
