import re


class PythonValidationAdapter:

    _EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def is_email(self, text: str) -> bool:
        return bool(self._EMAIL_PATTERN.match(text))

    def is_numeric(self, text: str) -> bool:
        return text.isnumeric()

    def is_not_empty(self, text: str) -> bool:
        return len(text.strip()) > 0

    def min_length(self, text: str, length: int) -> bool:
        return len(text) >= length

    def max_length(self, text: str, length: int) -> bool:
        return len(text) <= length
