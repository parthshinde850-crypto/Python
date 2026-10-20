# calculator.py

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a, b):
    return a *b
def divide(a,b):
    return a/b

# main.py
import calculatou
a = float(input("enter first number:"))
b = float(input("enter second number:"))
print("addition:", calculatou.add(a,b))
print("substraction:", calculatou.subtract(a,b))
print("multiplication", calculatou.multiply(a,b))
print("Divide:", calculatou.divide(a,b))