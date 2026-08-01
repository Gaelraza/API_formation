from abc import ABC, abstractmethod


class DatabaseInterface(ABC):

    @abstractmethod
    def create(self, table: str, data: dict) -> dict:
        raise NotImplementedError

    @abstractmethod
    def read(self, table: str, record_id: str) -> dict:
        raise NotImplementedError

    @abstractmethod
    def update(self, table: str, record_id: str, data: dict) -> dict:
        raise NotImplementedError

    @abstractmethod
    def delete(self, table: str, record_id: str) -> None:
        raise NotImplementedError
