from capability.validation.abstraction import ValidationAbstraction
from capability.validation.adapters.python_validation_adapter import PythonValidationAdapter


def execute(payload: dict) -> dict:
    if "text" not in payload:
        return {"success": False, "error": {"code": "MISSING_FIELD", "message": "Missing required field: text"}}
    if not isinstance(payload["text"], str):
        return {"success": False, "error": {"code": "INVALID_TYPE", "message": "Invalid type for field: text, expected str"}}

    try:
        abstraction = ValidationAbstraction(PythonValidationAdapter())
        result = abstraction.is_numeric(payload["text"])
        return {"success": True, "data": {"result": result}}
    except TypeError:
        return {"success": False, "error": {"code": "VALIDATION_FAILED", "message": "A technical error occurred during validation"}}
