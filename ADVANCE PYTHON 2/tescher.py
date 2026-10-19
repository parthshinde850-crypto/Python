class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience  # in years

    def show_info(self):
        print("Name      :", self.name)
        print("Subject   :", self.subject)
        print("Experience:", f"{self.experience} years")
        print("---------------------------")

# create and display multiple teachers
t1 = Teacher("Mrs. Sharma", "Mathematics", 8)
t2 = Teacher("Mr. Desai", "Physics", 12)
t3 = Teacher("Ms. Rao", "English", 5)

t1.show_info()
t2.show_info()
t3.show_info()