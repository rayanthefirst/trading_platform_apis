from abc import ABC, abstractmethod

class TradingPlatform(ABC):
    """Abstract base class which encapsulates necessary functions from trading platforms"""
    
    @abstractmethod
    def connect():
        ...

    @abstractmethod
    def terminate_connection():
        ...

    @abstractmethod
    def get_portfolio():
        ...

    @abstractmethod
    def get_min_order():
        ...
    
    @abstractmethod
    def place_market_order():
        ...

    