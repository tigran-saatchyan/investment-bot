import requests

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

def handle_ticker_request(chat_id: int, ticker_symbol: str):
    response = requests.get(f"http://ticker-service/ticker/{ticker_symbol}")
    data = response.json()
    send_message(chat_id, data)

def handle_news_request(chat_id: int):
    response = requests.get(f"http://investment-news-service/news")
    data = response.json()
    send_message(chat_id, data)

def send_message(chat_id: int, data: dict):
    text = "\n".join([f"{key}: {value}" for key, value in data.items()])
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)
