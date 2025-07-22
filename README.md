**Alertmanager + Telegram Integration**
Dockerized solution for sending Prometheus alerts to Telegram

🚀 Quick Start
============================================================
docker-compose up -d --build

🔧Configuration
===========================================================
Environment Variables
Create .env file:

***!!! OR JUST ADD YOUR TOKEN AND CHAT INTO py FILE !!!***

TELEGRAM_TOKEN=your_bot_token  
CHAT_ID=your_chat_id  

Docker Compose
Manages two services:
Alertmanager (port 9093)
Telegram webhook (port 8080)

⚙️ Integration Guide
Prometheus Setup
============================================================
Add to your prometheus.yml:

alerting:
  alertmanagers:
  - static_configs:
    - targets: ['localhost:9093'] 
      
Auto-start (Linux)
============================================================

sudo cp alertmanager-telegramm.service /etc/systemd/system/

sudo systemctl enable --now alertmanager-telegramm.service

🛠️ Verification
============================================================
Send test alert:

curl -X POST http://localhost:9093/api/v1/alerts -d '[{"labels":{"alertname":"TEST"}}]'

Check Telegram for notification

⚠️ Troubleshooting
============================================================

No Telegram alerts        -        **!!! Verify bot token/chat_id !!!** = .env it may work incorrectly

Alertmanager unreachable        -        Check Docker network connectivity

Service won't start        -        Inspect logs: journalctl -u alertmanager-telegramm.service OR docker logs telegram-webhook OR docker logs alertmanager
