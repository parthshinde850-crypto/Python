class Employee:
    language = "py" #This is class attribute
    salary = 12000000000000


parth = Employee()
parth.name = "Parth" #This is object instance attribute
print(parth.name, parth.language, parth.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here name is object/ instance attribute and salary and language are class attributes as they directly belong 
# to the class