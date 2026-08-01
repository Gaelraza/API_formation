from capability.database.abstraction import DatabaseAbstraction
from capability.database.adapters.sqlite_adapter import SQLiteAdapter


def execute(payload: dict) -> dict:
    if "table" not in payload:
        return {"success": False, "error": {"code": "MISSING_FIELD", "message": "Missing required field: table"}}
    if not isinstance(payload["table"], str):
        return {"success": False, "error": {"code": "INVALID_TYPE", "message": "Invalid type for field: table, expected str"}}
    if not payload["table"]:
        return {"success": False, "error": {"code": "INVALID_VALUE", "message": "Invalid value for field: table, cannot be empty"}}
    if "data" not in payload:
        return {"success": False, "error": {"code": "MISSING_FIELD", "message": "Missing required field: data"}}
    if not isinstance(payload["data"], dict):
        return {"success": False, "error": {"code": "INVALID_TYPE", "message": "Invalid type for field: data, expected dict"}}

    try:
        abstraction = DatabaseAbstraction(SQLiteAdapter())
        result = abstraction.create(payload["table"], payload["data"])
        return {"success": True, "data": {"result": result}}
    except (TypeError, RuntimeError):
        return {"success": False, "error": {"code": "DATABASE_FAILED", "message": "A technical error occurred during database operation"}}
