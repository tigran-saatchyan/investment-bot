import yfinance as yf
from app.strategy import TickerStrategy

# Concrete implementation of the TickerStrategy using yfinance
class YFinanceStrategy(TickerStrategy):
    def get_ticker_data(self, symbol: str):
        ticker = yf.Ticker(symbol)
        price = ticker.history(period="1d")['Close'][0]
        return price
