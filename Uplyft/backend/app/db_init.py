import pandas as pd
import os
from app import create_app, db
from app.models import Product, User

app = create_app()

def load_mock_data():
    with app.app_context():
        db.drop_all()
        db.create_all()

        print("Tables created.")

        # Load products
        csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'mock_data', 'products.csv'))
        df = pd.read_csv(csv_path)

        for _, row in df.iterrows():
            p = Product(**row.to_dict())
            db.session.add(p)

        # Add test user
        user = User(username='testuser', password='testpass')
        db.session.add(user)

        db.session.commit()
        print("Mock data and user inserted.")

if __name__ == '__main__':
    load_mock_data()


