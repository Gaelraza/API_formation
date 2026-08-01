from flask import Flask, request, jsonify

from business_logic.transformation import (
    uppercase_transformation,
    lowercase_transformation,
    capitalize_transformation,
    trim_transformation,
    replace_transformation,
    reverse_transformation,
)

app = Flask(__name__)

ROUTING_TABLE = {
    "uppercase": uppercase_transformation.execute,
    "lowercase": lowercase_transformation.execute,
    "capitalize": capitalize_transformation.execute,
    "trim": trim_transformation.execute,
    "replace": replace_transformation.execute,
    "reverse": reverse_transformation.execute,
}


@app.route("/transform", methods=["POST"])
def transform():
    # 2. Parse JSON body
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({
            "success": False,
            "error": {
                "code": "INVALID_JSON",
                "message": "Request body must be a valid JSON object"
            }
        }), 400

    # 3. Extract "operation" field
    if "operation" not in payload:
        return jsonify({
            "success": False,
            "error": {
                "code": "MISSING_OPERATION",
                "message": "Missing required field: operation"
            }
        }), 400

    operation = payload["operation"]

    # 4. Look up operation in routing table
    if operation not in ROUTING_TABLE:
        return jsonify({
            "success": False,
            "error": {
                "code": "UNKNOWN_OPERATION",
                "message": f"Unknown operation: {operation}"
            }
        }), 400

    # 5. Call the matched business_logic module's execute(payload)
    result = ROUTING_TABLE[operation](payload)

    # 6. Return the dict as HTTP JSON body with appropriate status code
    status_code = 200 if result.get("success") is True else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
