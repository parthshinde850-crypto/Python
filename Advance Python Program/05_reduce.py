from functools import reduce

l = [111, 2, 65, 635, 53, 65, 74, 45, 55]

def greatest(a,b ):
    if (a>b):
        return a
    return b

print(reduce(greatest, l))