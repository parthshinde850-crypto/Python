# Stack implementation using list

stack = []

# Push operation
def push(item):
    stack.append(item)
    print(f"{item} pushed into stack")

# Pop operation
def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print(f"{stack.pop()} popped from stack")

# Peek operation
def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print(f"Top element is {stack[-1]}")

# Display stack
def display():
    print("Stack:", stack)

# Example usage
push(10)
push(20)
push(30)
display()

peek()
pop()
display()