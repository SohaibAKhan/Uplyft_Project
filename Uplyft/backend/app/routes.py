from flask import Blueprint, request, jsonify
from .models import Product, User
from .utils import authenticate, parse_query
from flask_jwt_extended import jwt_required, create_access_token
from . import db

api = Blueprint('api', __name__)

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400

    token = authenticate(username, password, db)

    if token:
        return jsonify(access_token=token)
    return jsonify({'msg': 'Invalid credentials'}), 401

@api.route('/chat', methods=['POST'])
@jwt_required()
def chat():
    query = request.json.get('message', '')
    filters = parse_query(query)
    q = db.session.query(Product)

    if 'category' in filters:
        q = q.filter(Product.category.ilike(f"%{filters['category']}%"))
    if 'price' in filters:
        q = q.filter(Product.price <= filters['price'])

    results = q.limit(10).all()
    products = [{
        'name': p.name,
        'category': p.category,
        'price': p.price,
        'description': p.description,
        'image_url': p.image_url
    } for p in results]

    return jsonify(products)
