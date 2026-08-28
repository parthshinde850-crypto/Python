import matplotlib.pyplot as plt

# Sample data
products = ["Shampoo", "Soap", "Oil", "Toothpaste", "Biscuits"]
sales = [50, 80, 30, 60, 90]

# Create bar chart
plt.bar(products, sales)

# Labels and title
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales of Different Products in a Store")

plt.show()