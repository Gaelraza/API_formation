from flask import Flask, request, jsonify

from business_logic.transformation import (
    uppercase_transformation,
    lowercase_transformation,
    capitalize_transformation,
    trim_transformation,
    replace_transformation,
    reverse_transformation,
    swapcase_transformation,
    titlecase_transformation,
    length_transformation,
)

from business_logic.authentication import (
    generate_token_authentication,
    verify_token_authentication,
)

app = Flask(__name__)

ROUTING_TABLE = {
    "uppercase": uppercase_transformation.execute,
    "lowercase": lowercase_transformation.execute,
    "capitalize": capitalize_transformation.execute,
    "trim": trim_transformation.execute,
    "replace": replace_transformation.execute,
    "reverse": reverse_transformation.execute,
    "swapcase": swapcase_transformation.execute,
    "titlecase": titlecase_transformation.execute,
    "length": length_transformation.execute,
}

AUTH_ROUTING_TABLE = {
    "generate": generate_token_authentication.execute,
    "verify": verify_token_authentication.execute,
}


@app.route("/transform", methods=["POST"])
def transform():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({
            "success": False,
            "error": {
                "code": "INVALID_JSON",
                "message": "Request body must be a valid JSON object"
            }
        }), 400

    if "operation" not in payload:
        return jsonify({
            "success": False,
            "error": {
                "code": "MISSING_OPERATION",
                "message": "Missing required field: operation"
            }
        }), 400

    operation = payload["operation"]

    if operation not in ROUTING_TABLE:
        return jsonify({
            "success": False,
            "error": {
                "code": "UNKNOWN_OPERATION",
                "message": f"Unknown operation: {operation}"
            }
        }), 400

    result = ROUTING_TABLE[operation](payload)

    status_code = 200 if result.get("success") is True else 400
    return jsonify(result), status_code


@app.route("/authenticate", methods=["POST"])
def authenticate():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"success": False, "error": {"code": "INVALID_JSON", "message": "Request body must be a valid JSON object"}}), 400

    if "operation" not in payload:
        return jsonify({"success": False, "error": {"code": "MISSING_OPERATION", "message": "Missing required field: operation"}}), 400

    operation = payload["operation"]

    if operation not in AUTH_ROUTING_TABLE:
        return jsonify({"success": False, "error": {"code": "UNKNOWN_OPERATION", "message": f"Unknown operation: {operation}"}}), 400

    result = AUTH_ROUTING_TABLE[operation](payload)
    status_code = 200 if result.get("success") is True else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
