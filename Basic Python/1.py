class Product:
    def __init__(self, Product_Name, Product_ID, Price):
        self.Product_Name = Product_Name
        self.Product_ID = Product_ID
        self.Price = Price

    def get_category(self):
        if self.Price >= 50000:
            return "Premium"
        elif self.Price >= 10000:
            return "Standard"
        else:
            return "Budget"
        
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.Product_Name} | {self.Product_ID} | {self.Price} | {self.get_category()}"


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)

    def display_all(self):
        for product in self.products:
            print(product)

n = int(input())

cart = ShoppingCart()

for _ in range(n):
    data = input().split(",")

    name = data[0]
    product_id = data[1]
    price = int(data[2])

    product = Product(name, product_id, price)
    cart.add_product(product)

cart.display_all()