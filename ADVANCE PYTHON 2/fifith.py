class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)

# Create object
c1 = Car("Tata", "Nexon")

# Call method
c1.display()