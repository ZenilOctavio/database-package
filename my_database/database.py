from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self, host: str, username: str, password: str, database: str) -> None:
        pass
    
    @abstractmethod
    def disconnect(self) -> None:
        pass
    
    @abstractmethod
    def select(self, query: str) -> list:
        pass
    
    @abstractmethod
    def insert(self, script: str) -> None:
        pass

    @abstractmethod
    def delete(self, script: str) -> None:
        pass

    @abstractmethod
    def update(self, script: str) -> None:
        pass