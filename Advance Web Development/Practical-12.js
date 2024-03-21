function Restaurant() {
    this.tables = {};
  }
  
  Restaurant.prototype.addTable = function(tableNum, numOfPersons) {
    this.tables[tableNum] = {
      numOfPersons: numOfPersons,
      orders: []
    };
  };
  
  Restaurant.prototype.addOrder = function(tableNum, itemName, price) {
    this.tables[tableNum].orders.push({
      itemName: itemName,
      price: price
    });
  };
  
  Restaurant.prototype.getTotalBill = function(tableNum) {
    let bill = 0;
    this.tables[tableNum].orders.forEach(function(order) {
      bill += order.price;
    });
    return bill;
  };
  
  Restaurant.prototype.getTip = function(tableNum) {
    let bill = this.getTotalBill(tableNum);
    let tip = 0;
    if (bill < 500) {
      tip = 0.1 * bill;
    } else if (bill >= 500 && bill < 1000) {
      tip = 0.15 * bill;
    } else if (bill >= 1000 && bill < 1500) {
      tip = 0.18 * bill;
    } else {
      tip = 0.2 * bill;
    }
    return tip;
  };
  
  let restaurant = new Restaurant();
  
  
  restaurant.addTable(1, 4);
  
  restaurant.addOrder(1, "Pizaa", 400);
  restaurant.addOrder(1, "Coke", 50);
  restaurant.addOrder(1, "Paneer Tikka", 300);
  restaurant.addOrder(1, "Garlic Naan", 60);
  
  let totalBill = restaurant.getTotalBill(1);
  let tip = restaurant.getTip(1);
  console.log("Table Number: 1");
  console.log("Number of Persons: 4");
  console.log("Orders:");
  let orders = restaurant.tables[1].orders;
  orders.forEach(function(order, index) {
    console.log((index + 1) + ". " + order.itemName + " - " + order.price);
  });
  console.log("Total Bill: " + totalBill);
  console.log("Tip: " + tip);
  