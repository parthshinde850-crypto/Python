#greetings.py

def morning_greeting(name):
    return f"good morning,{name}!"
def evening_greeting(name):
    return f"good evening,{name}!"

#main.py

import greeting

name = input("enter your name:")
print(greeting.morning_greeting(name))
print(greeting.evening_greeting(name))