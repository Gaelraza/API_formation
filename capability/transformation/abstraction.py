from capability.transformation.interface import TransformationInterface


class TransformationAbstraction(TransformationInterface):
    """
    Concrete implementation of TransformationInterface that delegates
    all transformation operations to an injected adapter.
    """

    def __init__(self, adapter: TransformationInterface) -> None:
        self._adapter = adapter

    def to_upper(self, text: str) -> str:
        return self._adapter.to_upper(text)

    def to_lower(self, text: str) -> str:
        return self._adapter.to_lower(text)

    def to_capitalized(self, text: str) -> str:
        return self._adapter.to_capitalized(text)

    def to_trimmed(self, text: str) -> str:
        return self._adapter.to_trimmed(text)

    def to_replaced(self, text: str, target: str, replacement: str) -> str:
        return self._adapter.to_replaced(text, target, replacement)

    def to_reversed(self, text: str) -> str:
        return self._adapter.to_reversed(text)

    def to_swapcase(self, text: str) -> str:
        return self._adapter.to_swapcase(text)

    def to_titlecase(self, text: str) -> str:
        return self._adapter.to_titlecase(text)

    def to_length(self, text: str) -> int:
        return self._adapter.to_length(text)
