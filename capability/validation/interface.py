from abc import ABC, abstractmethod


class ValidationInterface(ABC):

    @abstractmethod
    def is_email(self, text: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def is_numeric(self, text: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def is_not_empty(self, text: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def min_length(self, text: str, length: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    def max_length(self, text: str, length: int) -> bool:
        raise NotImplementedError
