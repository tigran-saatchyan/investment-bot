from abc import ABC, abstractmethod

# Defines the strategy interface for fetching ticker data
class TickerStrategy(ABC):
    @abstractmethod
    def get_ticker_data(self, symbol: str):
        pass
