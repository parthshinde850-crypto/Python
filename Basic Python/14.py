# 14. Method overriding
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog: Woof Woof")

class Cat(Animal):
    def sound(self):
        print("Cat: Meow")

# Demo
a = Animal()
d = Dog()
c = Cat()

a.sound()   # Some generic animal sound
d.sound()   # Dog: Woof Woof
c.sound()   # Cat: Meow