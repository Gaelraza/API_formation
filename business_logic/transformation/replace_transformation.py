from capability.transformation.abstraction import TransformationAbstraction
from capability.transformation.adapters.python_string_adapter import PythonStringAdapter


def execute(payload: dict) -> dict:
    for field in ("text", "target", "replacement"):
        if field not in payload:
            return {"success": False, "error": {"code": "MISSING_FIELD", "message": f"Missing required field: {field}"}}
        if not isinstance(payload[field], str):
            return {"success": False, "error": {"code": "INVALID_TYPE", "message": f"Invalid type for field: {field}, expected str"}}

    if not payload["target"]:
        return {"success": False, "error": {"code": "INVALID_VALUE", "message": "target cannot be empty"}}

    try:
        abstraction = TransformationAbstraction(PythonStringAdapter())
        result = abstraction.to_replaced(payload["text"], payload["target"], payload["replacement"])
        return {"success": True, "data": {"result": result}}
    except TypeError:
        return {"success": False, "error": {"code": "TRANSFORMATION_FAILED", "message": "A technical error occurred during transformation"}}
