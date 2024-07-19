from abc import ABC, abstractmethod

# Defines the strategy interface for fetching news
class NewsStrategy(ABC):
    @abstractmethod
    def get_news(self):
        pass
