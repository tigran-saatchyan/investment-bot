import os

# Configuration for the Investment News service
class Config:
    NEWS_SERVICE_PORT = os.getenv("NEWS_SERVICE_PORT", 8003)
