class Employee:
    a = 1 


    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45
e.show()
#If @classmethod not use then output get 45 because we know that intrinsic value get print or output