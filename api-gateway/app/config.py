import os

# Configuration for the API Gateway service
class Config:
    API_GATEWAY_PORT = os.getenv("API_GATEWAY_PORT", 8000)
