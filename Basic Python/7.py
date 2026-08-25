class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("-----------------------")

# Creating multiple student objects
s1 = Student("Parth", 1, 85)
s2 = Student("Aniket", 2, 90)
s3 = Student("Riya", 3, 88)

# Displaying details
s1.display()
s2.display()
s3.display()