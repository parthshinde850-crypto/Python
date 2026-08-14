class Employee:
    language = "Python" #This is class attribute
    salary = 12000000000000


parth = Employee()
parth.language = "Javascript" #This is instance attribute
print(parth.language, parth.salary)


# Here instance attributes take preference over class attribute

# it check whether instance attribute present or not if not it print class attribute