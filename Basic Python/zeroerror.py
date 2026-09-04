try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = num1 / num2
    print("Result is:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")