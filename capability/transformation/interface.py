from abc import ABC, abstractmethod


class TransformationInterface(ABC):
    """
    Abstract base class defining the six transformation primitives.
    """

    @abstractmethod
    def to_upper(self, text: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def to_lower(self, text: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def to_capitalized(self, text: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def to_trimmed(self, text: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def to_replaced(self, text: str, target: str, replacement: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def to_reversed(self, text: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def to_swapcase(self, text: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def to_titlecase(self, text: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def to_length(self, text: str) -> int:
        raise NotImplementedError
