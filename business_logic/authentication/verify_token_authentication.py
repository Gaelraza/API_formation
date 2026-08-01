import jwt

from capability.authentication.abstraction import AuthenticationAbstraction
from capability.authentication.adapters.pyjwt_adapter import PyJWTAdapter


def execute(payload: dict) -> dict:
    if "token" not in payload:
        return {"success": False, "error": {"code": "MISSING_FIELD", "message": "Missing required field: token"}}
    if not isinstance(payload["token"], str):
        return {"success": False, "error": {"code": "INVALID_TYPE", "message": "Invalid type for field: token, expected str"}}

    try:
        abstraction = AuthenticationAbstraction(PyJWTAdapter())
        result = abstraction.verify_token(payload["token"])
        return {"success": True, "data": {"result": result}}
    except jwt.ExpiredSignatureError:
        return {"success": False, "error": {"code": "TOKEN_EXPIRED", "message": "Token has expired"}}
    except jwt.InvalidTokenError:
        return {"success": False, "error": {"code": "INVALID_TOKEN", "message": "Token is invalid"}}
    except TypeError:
        return {"success": False, "error": {"code": "AUTH_FAILED", "message": "A technical error occurred during authentication"}}
