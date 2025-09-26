from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")  # Get token from Railway environment variable

FAQS = {
    "what is reya dex": "Reya Dex is a decentralized exchange (DEX) for trading crypto assets.",
    "how to trade": "To trade on Reya Dex, connect your wallet and choose the pair you want to trade.",
    "fees": "Reya Dex charges low fees compared to centralized exchanges.",
    "support": "For support, visit the official Reya Dex community or docs."
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm your ReyaDex FAQ bot. Use /ask <question>")

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Example: /ask what is reya dex")
        return
    question = " ".join(context.args).lower()
    answer = FAQS.get(question, "Sorry, I don’t have an answer for that yet.")
    await update.message.reply_text(answer)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ask", ask))
    app.run_polling()

if __name__ == "__main__":
    main()
