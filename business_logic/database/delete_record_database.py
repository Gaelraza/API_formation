from capability.database.abstraction import DatabaseAbstraction
from capability.database.adapters.sqlite_adapter import SQLiteAdapter


def execute(payload: dict) -> dict:
    if "table" not in payload:
        return {"success": False, "error": {"code": "MISSING_FIELD", "message": "Missing required field: table"}}
    if not isinstance(payload["table"], str):
        return {"success": False, "error": {"code": "INVALID_TYPE", "message": "Invalid type for field: table, expected str"}}
    if not payload["table"]:
        return {"success": False, "error": {"code": "INVALID_VALUE", "message": "Invalid value for field: table, cannot be empty"}}
    if "record_id" not in payload:
        return {"success": False, "error": {"code": "MISSING_FIELD", "message": "Missing required field: record_id"}}
    if not isinstance(payload["record_id"], str):
        return {"success": False, "error": {"code": "INVALID_TYPE", "message": "Invalid type for field: record_id, expected str"}}

    try:
        abstraction = DatabaseAbstraction(SQLiteAdapter())
        result = abstraction.delete(payload["table"], payload["record_id"])
        return {"success": True, "data": {"result": result}}
    except LookupError:
        return {"success": False, "error": {"code": "RECORD_NOT_FOUND", "message": "Record not found"}}
    except (TypeError, RuntimeError):
        return {"success": False, "error": {"code": "DATABASE_FAILED", "message": "A technical error occurred during database operation"}}
