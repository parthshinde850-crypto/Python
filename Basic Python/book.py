class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("Title :", self.title)
        print("Author:", self.author)
        print("Price :", self.price)
        print("---------------------------")

# create and display at least three books
b1 = Book("The Alchemist", "Paulo Coelho", 299.0)
b2 = Book("Atomic Habits", "James Clear", 599.0)
b3 = Book("Python Crash Course", "Eric Matthes", 899.0)

b1.display_details()
b2.display_details()
b3.display_details()