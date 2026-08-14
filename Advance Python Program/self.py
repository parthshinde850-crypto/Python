class Employee:
    language = "Python" #This is class attribute 
    salary = 120000000

    def getInfo(self): #if self not use then error shown 
        print(f"The language is {self.language}. The salary is {self.salary}")

    def great(self):
        print("Good Morining")
parth = Employee()
parth.language = "Javascript" #This is instance attribute

parth.great()
parth.getInfo()
Employee.getInfo(parth) #both work same tast and print same output