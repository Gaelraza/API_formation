from capability.validation.interface import ValidationInterface


class ValidationAbstraction(ValidationInterface):

    def __init__(self, adapter: ValidationInterface) -> None:
        self._adapter = adapter

    def is_email(self, text: str) -> bool:
        return self._adapter.is_email(text)

    def is_numeric(self, text: str) -> bool:
        return self._adapter.is_numeric(text)

    def is_not_empty(self, text: str) -> bool:
        return self._adapter.is_not_empty(text)

    def min_length(self, text: str, length: int) -> bool:
        return self._adapter.min_length(text, length)

    def max_length(self, text: str, length: int) -> bool:
        return self._adapter.max_length(text, length)
