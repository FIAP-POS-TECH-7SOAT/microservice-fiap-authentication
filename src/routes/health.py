from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health():
    result = {
        "success": True
    }
    
    return jsonify(result), 201