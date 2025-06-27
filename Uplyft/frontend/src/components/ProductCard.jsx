import React from 'react';

export default function ProductCard({ name, price, category, description, image_url }) {
  return (
    <div className="bg-white p-4 rounded shadow">
      <img src={image_url} alt={name} className="w-full h-40 object-cover rounded mb-2" />
      <h2 className="font-bold text-lg">{name}</h2>
      <p className="text-sm text-gray-500">{category}</p>
      <p className="text-sm">{description}</p>
      <p className="font-semibold mt-1">₹{price.toFixed(2)}</p>
    </div>
  );
}
