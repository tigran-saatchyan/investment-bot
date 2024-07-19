import os

# Configuration for the Telegram Bot service
class Config:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_BOT_PORT = os.getenv("TELEGRAM_BOT_PORT", 8001)
