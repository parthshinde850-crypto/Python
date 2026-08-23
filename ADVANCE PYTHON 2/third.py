class Student:
    def getData(self, name, age):
        self.name = name
        self.age = age

    
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student()

s1.getData("parth", 20)
s1.display()