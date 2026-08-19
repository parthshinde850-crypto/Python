class Student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def display(self):
        print("Student Details")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Roll No :", self.roll_no)



student1 = Student("Parth", 20, 33)
Student2 = Student("aditya",20,31)

student1.display()
Student2.display()