class PythonStringAdapter:
    """
    Concrete adapter implementing string transformations using Python built-ins.
    """

    def to_upper(self, text: str) -> str:
        return text.upper()

    def to_lower(self, text: str) -> str:
        return text.lower()

    def to_capitalized(self, text: str) -> str:
        return text[:1].upper() + text[1:] if text else text

    def to_trimmed(self, text: str) -> str:
        return text.strip()

    def to_replaced(self, text: str, target: str, replacement: str) -> str:
        return text.replace(target, replacement)

    def to_reversed(self, text: str) -> str:
        return text[::-1]
