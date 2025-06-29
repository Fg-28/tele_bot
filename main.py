from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

@app.route('/')
def home():
    return "VenusBot is running!"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "").lower()

        if text == "/start":
            reply = """Thanks for visiting VenusBot! 🤖

Here are the available triggers:

🔹 /top10 — Top 10 highest expense branches  
🔹 /summary — Summary report  
🔹 /last10 — Least expense branches"""
        elif text == "/top10":
            reply = "🧾 Top 10 branches by expenses:\n1. Branch A...\n(etc...)"
        elif text == "/summary":
            reply = "📊 Expense Summary:\nTotal: ₹X\nCleared: ₹Y\nPending: ₹Z"
        elif text == "/last10":
            reply = "💸 Least 10 expense branches:\n1. Branch Z...\n(etc...)"
        else:
            reply = "❓ Unknown command. Type /start to see options."

        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": chat_id,
            "text": reply
        })

    return "ok", 200

# 🚨 REQUIRED for Railway to work:
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
