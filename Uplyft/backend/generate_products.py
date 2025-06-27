import csv
import random
import os

# Create mock_data folder if it doesn't exist
output_dir = os.path.join(os.path.dirname(__file__), '..', 'mock_data')
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, 'products.csv')

categories = {
    'electronics': ['Smartphone', 'Laptop', 'Headphones', 'Monitor'],
    'books': ['Fiction', 'Non-Fiction', 'Biography', 'Science'],
    'fashion': ['T-Shirt', 'Shoes', 'Jacket', 'Jeans']
}

names = {
    'electronics': ['Redmi', 'Samsung', 'HP', 'Dell', 'Boat', 'Sony'],
    'books': ['The Alchemist', 'Sapiens', 'Atomic Habits', 'Think Big'],
    'fashion': ['Nike', 'Adidas', 'Puma', 'Levi\'s', 'Zara']
}

with open(output_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'name', 'category', 'price', 'description', 'image_url'])

    for i in range(1, 121):
        category = random.choice(list(categories.keys()))
        item_type = random.choice(categories[category])
        brand = random.choice(names[category])
        name = f"{brand} {item_type}"
        price = round(random.uniform(199, 49999), 2)
        desc = f"{item_type} by {brand}, high quality and stylish"
        img_url = f"https://picsum.photos/200?random={i}"
        writer.writerow([i, name, category, price, desc, img_url])

print(f"✔️ Generated mock product data at: {output_path}")
