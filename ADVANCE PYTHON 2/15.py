# 15. Polymorphism with common interface
class Car:
    def move(self):
        print("Car is moving on 4 wheels")

class Bike:
    def move(self):
        print("Bike is moving on 2 wheels")

def perform_move(vehicle):
    # works for any object that has move()
    vehicle.move()

# Demo with multiple objects
v1 = Car()
v2 = Bike()
objects = [v1, v2]

for obj in objects:
    perform_move(obj)

# Output:
# Car is moving on 4 wheels
# Bike is moving on 2 wheels