a = 89  #Global variable 

def fun():
    global a  # change the global variable ( a = 89 to a = 3 )
    a = 3. # Local variable in def function
    print(a)

fun()
print(a)