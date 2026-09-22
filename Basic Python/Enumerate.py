lst = [ 3, 513, 53, 535]

# index = 0
# for item in lst:
    # print(f"The item number at index {index} is {item}")
    # index += 1

# This can be simplified by using enumerate function

for index , item in enumerate(lst):
    print(f"The item number at index {index} is {item}")