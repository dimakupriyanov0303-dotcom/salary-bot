from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "ТВОЙ_ТОКЕН"

WEBAPP_URL = "http://127.0.0.1:5000"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = ReplyKeyboardMarkup(
        [[KeyboardButton("📅 Открыть календарь", web_app=WebAppInfo(url=WEBAPP_URL))]],
        resize_keyboard=True
    )

    await update.message.reply_text("💰 WebApp готов", reply_markup=keyboard)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot started...")
app.run_polling()