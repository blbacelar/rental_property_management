from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from services.tenant_service import (add_tenant, assign_tenant_to_property,
                                     get_tenants)

tenant_bp = Blueprint('tenant', __name__)

@tenant_bp.route('/tenants', methods=['POST'])
@jwt_required()
def add_tenant_route():
    data = request.json
    tenant, error = add_tenant(data['name'], data['email'], data.get('property_id'))
    if error:
        return jsonify({'error': error}), 400
    return jsonify(tenant.to_dict()), 201

@tenant_bp.route('/tenants', methods=['GET'])
@jwt_required()
def get_tenants_route():
    tenants = get_tenants()
    return jsonify(tenants), 200

@tenant_bp.route('/tenants/<int:tenant_id>/assign', methods=['PUT'])
@jwt_required()
def assign_tenant_route(tenant_id):
    data = request.json
    tenant, error = assign_tenant_to_property(tenant_id, data['property_id'])
    if error:
        return jsonify({'error': error}), 400
    return jsonify(tenant.to_dict()), 200
