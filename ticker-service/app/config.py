import os

# Configuration for the Ticker service
class Config:
    TICKER_SERVICE_PORT = os.getenv("TICKER_SERVICE_PORT", 8002)
