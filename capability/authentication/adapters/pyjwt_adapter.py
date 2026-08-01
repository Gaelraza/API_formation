import os

import jwt


class PyJWTAdapter:

    def __init__(self) -> None:
        secret_key = os.environ.get("AUTH_SECRET_KEY")
        if not secret_key:
            raise RuntimeError("AUTH_SECRET_KEY environment variable is not set")
        self._secret_key = secret_key

    def generate_token(self, claims: dict) -> str:
        return jwt.encode(claims, self._secret_key, algorithm="HS256")

    def verify_token(self, token: str) -> dict:
        return jwt.decode(token, self._secret_key, algorithms=["HS256"])
