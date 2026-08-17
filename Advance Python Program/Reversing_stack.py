# Reverse stack using another stack

stack = [10, 20, 30, 40]

temp_stack = []

# Move elements to temp stack
while stack:
    temp_stack.append(stack.pop())

# Now temp_stack is reversed stack
stack = temp_stack

print("Reversed stack:", stack)