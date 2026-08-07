myList = [ 1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
    # squaredList.append(item*item)
    
#This can be done in easiest way by using list comprehensions .

squaredList = [i*i for i in myList]
print(squaredList)