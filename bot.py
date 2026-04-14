from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8404255420:AAFn1TXIX47O_VT3BfeB2bIrrl_CQ76t0mc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton(
            "📊 Открыть калькулятор",
            web_app=WebAppInfo(url="https://YOUR-RENDER-LINK.onrender.com")
        )]
    ], resize_keyboard=True)

    await update.message.reply_text("💰 Бот зарплаты запущен", reply_markup=keyboard)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot started")
app.run_polling()