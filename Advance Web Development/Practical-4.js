const cart = {
    groceries: [
      { name: "Milk", price: 50, quantity: 2 },
      { name: "Bread", price: 60, quantity: 3 },
      { name: "Chips Packets", price: 10, quantity: 12 }
    ],
    apparels: [
      { name: "T-Shirt", price: 500, quantity: 1 },
      { name: "Jeans", price:  1000, quantity: 1 }
    ],
    accessories: [
      { name: "Watch", price: 3500, quantity: 1 },
      { name: "Sunglasses", price: 1500, quantity: 2 }
    ],
    gadgets: [
      { name: "Laptop", price: 750000, quantity: 1 },
      { name: "Smartphone", price: 50000, quantity: 2 }
    ]
  };
  
  const discounts = {
    groceries: 0.1,
    apparels: 0.2,
    accessories: 0.05,
    gadgets: 0.5
  };
  
  let total = 0;
  
  
  for (const category in cart) {
    let categoryTotal = 0;
  
    for (const item of cart[category]) {
      categoryTotal += item.price * item.quantity;
    }
  
    categoryTotal *= 1 - discounts[category];
  
    console.log(`${category} total: ₹ ${categoryTotal.toFixed(2)}`);
    
  
    total += categoryTotal;
  }
  
  console.log(`\nTotal: ₹ ${total.toFixed(2)}`);
  