from capability.authentication.abstraction import AuthenticationAbstraction
from capability.authentication.adapters.pyjwt_adapter import PyJWTAdapter


def execute(payload: dict) -> dict:
    if "claims" not in payload:
        return {"success": False, "error": {"code": "MISSING_FIELD", "message": "Missing required field: claims"}}
    if not isinstance(payload["claims"], dict):
        return {"success": False, "error": {"code": "INVALID_TYPE", "message": "Invalid type for field: claims, expected dict"}}

    try:
        abstraction = AuthenticationAbstraction(PyJWTAdapter())
        result = abstraction.generate_token(payload["claims"])
        return {"success": True, "data": {"result": result}}
    except (TypeError, RuntimeError):
        return {"success": False, "error": {"code": "AUTH_FAILED", "message": "A technical error occurred during authentication"}}
