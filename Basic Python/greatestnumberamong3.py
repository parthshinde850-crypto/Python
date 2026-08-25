a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if a>=b and a>=c :
    print("Greatest number : " , a)
elif b>=a and b>=c :
    print("Greatest number ;" , b)
elif c>=a and c>=b :
    print("Greatest number : " , c)
else :
    print("All numbers are equal :")