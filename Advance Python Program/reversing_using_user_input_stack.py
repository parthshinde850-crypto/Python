# Take input
n = int(input("Enter number of elements: "))

stack = []
for i in range(n):
    x = int(input("Enter element: "))
    stack.append(x)

print("Original Stack:", stack)

# Reverse stack
stack.reverse()

print("Reversed Stack:", stack)