from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8404255420:AAFn1TXIX47O_VT3BfeB2bIrrl_CQ76t0mc"

WEBAPP_URL = "https://your-app.onrender.com"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = ReplyKeyboardMarkup(
        [[KeyboardButton("📅 Открыть календарь", web_app=WebAppInfo(url=WEBAPP_URL))]],
        resize_keyboard=True
    )

    await update.message.reply_text(
        "💰 Система расчёта зарплаты",
        reply_markup=keyboard
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("🤖 Bot started")

app.run_polling()
