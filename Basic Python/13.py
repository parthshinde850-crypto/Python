# 13. Method "overloading" using default arguments
class MathOperations:
    def add(self, a, b, c=0):
        """Add two or three numbers. If c not given, defaults to 0."""
        return a + b + c

# Demo
m = MathOperations()
print("Add 2 numbers (5 + 7)       =", m.add(5, 7))       # 12
print("Add 3 numbers (2 + 3 + 4)   =", m.add(2, 3, 4))    # 9

# Alternative using *args (flexible):
# def add(self, *nums):
#     return sum(nums)