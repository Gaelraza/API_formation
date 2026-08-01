from capability.transformation.abstraction import TransformationAbstraction
from capability.transformation.adapters.python_string_adapter import PythonStringAdapter


def execute(payload: dict) -> dict:
    if "text" not in payload:
        return {"success": False, "error": {"code": "MISSING_FIELD", "message": "Missing required field: text"}}
    if not isinstance(payload["text"], str):
        return {"success": False, "error": {"code": "INVALID_TYPE", "message": "Invalid type for field: text, expected str"}}

    try:
        abstraction = TransformationAbstraction(PythonStringAdapter())
        result = abstraction.to_swapcase(payload["text"])
        return {"success": True, "data": {"result": result}}
    except TypeError:
        return {"success": False, "error": {"code": "TRANSFORMATION_FAILED", "message": "A technical error occurred during transformation"}}
