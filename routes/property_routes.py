from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from services.property_service import (add_property, get_properties,
                                       upload_property_pictures)

property_bp = Blueprint('property', __name__)

@property_bp.route('/properties', methods=['POST'])
@jwt_required()
def add_property_route():
    data = request.json
    data['property_features'] = request.json.get('property_features', [])
    data['building_features'] = request.json.get('building_features', [])
    data['community_features'] = request.json.get('community_features', [])
    property = add_property(data)
    return jsonify(property.to_dict()), 201

@property_bp.route('/properties', methods=['GET'])
@jwt_required()
def get_properties_route():
    properties = get_properties()
    return jsonify(properties), 200

@property_bp.route('/properties/<int:property_id>/upload_pictures', methods=['POST'])
@jwt_required()
def upload_property_pictures_route(property_id):
    pictures = request.files.getlist('pictures')
    property, error = upload_property_pictures(property_id, pictures)
    if error:
        return jsonify({'error': error}), 400
    return jsonify(property.to_dict()), 200
