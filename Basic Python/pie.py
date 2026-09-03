import matplotlib.pyplot as plt

# Sample data
categories = ["Rent", "Food", "Travel", "Entertainment"]
expenses = [40, 25, 20, 15]

# Pie chart
plt.pie(expenses, labels=categories, autopct="%1.1f%%")

# Title
plt.title("Percentage Distribution of Monthly Expenses")

plt.show()