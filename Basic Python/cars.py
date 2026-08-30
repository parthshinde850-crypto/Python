class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Price :", self.price)
        print("---------------------------")

# create multiple car objects and display their info
c1 = Car("Maruti Suzuki", "Swift", 700000)
c2 = Car("Hyundai", "Creta", 1300000)
c3 = Car("Tata", "Nexon", 900000)

c1.display()
c2.display()
c3.display()