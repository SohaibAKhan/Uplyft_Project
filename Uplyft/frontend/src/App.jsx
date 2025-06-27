import React, { useState } from 'react';
import LoginForm from './components/LoginForm';
import ChatBot from './components/ChatBot';

export default function App() {
  const [token, setToken] = useState(localStorage.getItem('token'));

  const handleLogin = (newToken) => {
    localStorage.setItem('token', newToken);
    setToken(newToken);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <h1 className="text-3xl font-bold text-center mb-6">Uplyft Chatbot UI</h1>
      {!token ? <LoginForm onLogin={handleLogin} /> : <ChatBot token={token} />}
    </div>
  );
}
