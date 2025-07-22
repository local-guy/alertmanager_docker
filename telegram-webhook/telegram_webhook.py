from flask import Flask, request
import requests
import os


app = Flask(__name__)


BOT_TOKEN = "8111934398:AAESnyNCCyCpLZufHViUFAqLXDqqan5JHyY"
CHAT_ID = "-4955420023"

print(f"[DEBUG] BOT_TOKEN: {BOT_TOKEN}")
print(f"[DEBUG] CHAT_ID: {CHAT_ID}")

def send_telegram(text):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": text,
            "parse_mode": "HTML"
        }
        print(f"[DEBUG] Sending to Telegram: {payload}")
        resp = requests.post(url, json=payload)
        print(f"[Telegram] Status: {resp.status_code}, {resp.text}")
    except Exception as e:
        print(f"[Telegram] error:, {e}")

@app.route("/alert", methods=["POST"])
def alert():
    data = request.json
    print("Received alert:", data)
    for alert in data.get("alerts", []):
        msg = f"<b>{alert['status'].upper()}</b>: {alert['labels'].get('alertname')}\n"
        msg += f"<b>Уровень:</b> {alert['labels'].get('severity', 'N/A')}\n"
        msg += f"<b>Сводка:</b> {alert['annotations'].get('summary', '')}\n"
        msg += f"<b>Описание:</b> {alert['annotations'].get('description', '')}"
        print(f"[DEBUG] Constructed message:\n{msg}")
        send_telegram(msg)
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
