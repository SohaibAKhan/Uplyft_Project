# Uplyft Full Stack Intern Case Study

A full-stack e-commerce chatbot application where users can log in and search for products using natural language. The system responds with relevant product cards by parsing the query and filtering results from a mock database.

---

## Architecture Overview

React (Frontend) ↔ Flask (Backend API) ↔ SQLite (Database)

- Frontend: React app styled with Tailwind CSS using Vite for fast development.
- Backend: Flask API with JWT-based authentication and SQLAlchemy ORM.
- Database: SQLite loaded with mock data generated from CSV.

---

## Features

- User login with JWT authentication  
- Chatbot input for product search queries  
- Natural-language parsing into filters (price, category)  
- Products fetched from database and shown as cards  
- Responsive, clean frontend using Tailwind CSS  

---

## Tech Stack

Layer:       Tools & Libraries  
Frontend:    React (Vite), Tailwind CSS, Axios  
Backend:     Flask, Flask-JWT-Extended, SQLAlchemy, Pandas  
Database:    SQLite (with CSV mock data)  
Dev Tools:   Postman, PyCharm (Backend), VS Code (Frontend)  

---

## Project Structure

Uplyft/  
├── backend/  
│   ├── app/  
│   │   ├── models.py  
│   │   ├── routes.py  
│   │   ├── utils.py  
│   │   └── __init__.py  
│   ├── instance/ecommerce.db  
│   ├── db_init.py  
│   └── run.py  
│
|
├── frontend/  
│   ├── package.json  
│   ├── tailwind.config.js  
│   ├── vite.config.js  
│   ├── index.html  
│   └── src/  
│       ├── App.jsx  
│       ├── ChatBot.jsx  
│       ├── LoginForm.jsx  
│       └── ProductCard.jsx
│
|
├── mock_data/products.csv 

---

## Setup Instructions

### Backend

1. Install dependencies:  
   `pip install -r requirements.txt`

2. Generate mock data and create the database:  
   `python app/db_init.py`

3. Start the Flask API:  
   `python run.py`  
   The server runs at: http://localhost:5000

### Frontend

1. Install Node.js (https://nodejs.org) if not already installed

2. Navigate to the frontend directory:  
   `cd frontend`

3. Install dependencies:  
   `npm install`

4. Start the development server:  
   `npm run dev`  
   The app runs at: http://localhost:5173

---

## Testing the App

### Login Credentials

Username: testuser  
Password: testpass

### Example Queries

- show me books under 5000  
- laptops under 30000  
- tshirts  
- cheap shoes

The backend will parse the keywords and return filtered product data.

---

## Mock Data Details

Mock data includes randomized product names, categories, prices, and image URLs (via picsum.photos). Data is generated into a CSV file and imported into SQLite using Pandas and SQLAlchemy.

---

## Challenges Faced

- JWT format bug – fixed by ensuring `identity` is a string  
- No matching products – resolved by tuning mock data ranges  
- Frontend chat unresponsive – caused by browser ad blockers, fixed by whitelisting localhost 

---

## Optional Future Enhancements

- Add logout functionality and token expiry  
- Store chat history using localStorage  
- Improve filter extraction using NLP or LLM  
- Add product detail modals or routing  
- Deploy frontend to Vercel, backend to Render  

---

## Author

Sohaib Ahmed Khan

---

## License

This project is for educational and portfolio purposes under the MIT License.
