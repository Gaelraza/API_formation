from abc import ABC, abstractmethod


class AuthenticationInterface(ABC):

    @abstractmethod
    def generate_token(self, claims: dict) -> str:
        raise NotImplementedError

    @abstractmethod
    def verify_token(self, token: str) -> dict:
        raise NotImplementedError
