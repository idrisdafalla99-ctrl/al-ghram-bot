import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(
        f"مرحباً بك يا {user_name}!\n"
        "يعمل الآن بكفاءة (AL-GHRAM) بوت تداول 24/7 🚀"
    )

def main():
    token = "8412183406:AAFoifqLMZCMHwQ2UCaTU7sdWxk64SwW7-E" 
    
    if not token:
        print("Error: Token not found!")
        return

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    
    print("Telegram bot is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()
