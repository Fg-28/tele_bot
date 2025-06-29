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
        text = data["message"].get("text", "").strip().lower()

        if text == "/start":
            reply = """👋 Welcome to VenusBot!

Here are your available triggers:

🔹 /top10 – Top 10 highest expense branches  
🔹 /summary – Summary report  
🔹 /last10 – Least expense branches  

📩 You will not get reply here.  
Your report will be sent to your registered email."""

            requests.post(f"{TELEGRAM_API}/sendMessage", json={
                "chat_id": chat_id,
                "text": reply
            })

    return "ok", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
