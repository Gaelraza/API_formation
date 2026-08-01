from capability.authentication.interface import AuthenticationInterface


class AuthenticationAbstraction(AuthenticationInterface):

    def __init__(self, adapter: AuthenticationInterface) -> None:
        self._adapter = adapter

    def generate_token(self, claims: dict) -> str:
        return self._adapter.generate_token(claims)

    def verify_token(self, token: str) -> dict:
        return self._adapter.verify_token(token)
