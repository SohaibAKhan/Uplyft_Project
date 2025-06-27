import React, { useState } from 'react';
import axios from 'axios';
import ProductCard from './ProductCard';

export default function ChatBot({ token }) {
  const [message, setMessage] = useState('');
  const [results, setResults] = useState([]);

  const sendMessage = async () => {
    if (!message.trim()) return;
    try {
      const res = await axios.post(
        'http://localhost:5000/chat',
        { message },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setResults(res.data);
    } catch (err) {
      alert('Error sending message');
    }
  };

  return (
    <div className="max-w-2xl mx-auto space-y-4">
      <div className="flex gap-2">
        <input
          type="text"
          className="flex-1 border px-3 py-2 rounded"
          placeholder="Ask me something..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <button onClick={sendMessage} className="bg-green-600 text-white px-4 py-2 rounded">
          Send
        </button>
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {results.map((item, i) => (
          <ProductCard key={i} {...item} />
        ))}
      </div>
    </div>
  );
}
