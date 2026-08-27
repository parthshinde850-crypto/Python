def find_max_min(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum

# Example usage
lst = [23, 55, 12, 76, 34]
maximum, minimum = find_max_min(lst)
print("Maximum:", maximum)  # Output: Maximum: 76
print("Minimum:", minimum)  # Output: Minimum: 12
