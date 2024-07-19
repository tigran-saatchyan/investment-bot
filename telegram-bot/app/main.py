from fastapi import FastAPI, HTTPException
from app.handlers import handle_ticker_request, handle_news_request

app = FastAPI()


# Handles incoming webhooks from Telegram
@app.post("/telegram-webhook/")
async def telegram_webhook(update: dict):
    message = update.get("message")
    if not message:
        raise HTTPException(
            status_code=400, detail="No message found in update"
            )

    chat_id = message["chat"]["id"]
    text = message["text"]

    if text.startswith("/ticker"):
        ticker_symbol = text.split(" ")[1]
        handle_ticker_request(chat_id, ticker_symbol)
    elif text.startswith("/news"):
        handle_news_request(chat_id)

    return {"message": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
