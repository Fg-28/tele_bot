from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")

print("TOKEN CHECK:", repr(BOT_TOKEN))  # <-- Moved here

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """Thanks for visiting VenusBot! 🤖

Here are the available triggers:

🔹 /top10 — Top 10 highest expense branches  
🔹 /summary — Summary report  
🔹 /last10 — Least expense branches"""
    )

async def top10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧾 Top 10 branches by expenses:\n1. Branch A...\n(etc...)")

async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Expense Summary:\nTotal: ₹X\nCleared: ₹Y\nPending: ₹Z")

async def last10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💸 Least 10 expense branches:\n1. Branch Z...\n(etc...)")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("top10", top10))
app.add_handler(CommandHandler("summary", summary))
app.add_handler(CommandHandler("last10", last10))

app.run_polling()
