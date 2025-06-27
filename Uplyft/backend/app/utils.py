from flask_jwt_extended import create_access_token
import re

def authenticate(username, password, db):
    from .models import User
    user = db.session.query(User).filter_by(username=username, password=password).first()
    return create_access_token(identity=str(user.id)) if user else None

def parse_query(text):
    """
    Very basic keyword parser — you can extend this later or add LLM.
    """
    text = text.lower()
    filters = {}

    price_match = re.search(r'under\s+(\d+)', text)
    if price_match:
        filters['price'] = float(price_match.group(1))

    for cat in ['shoes', 'books', 'tshirts', 'laptops']:
        if cat in text:
            filters['category'] = cat
            break

    return filters
