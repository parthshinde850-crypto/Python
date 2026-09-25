class Animals:
    pass

class pets(Animals):
    pass

class Dog(pets):
    @staticmethod #def bark(self) use navta karay cha manun decorator use kela
    def bark():
        print("Bow Bow!")

d = Dog()
d.bark()
        