try :
    a = int(input("Enter a number:"))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else!")#Work if a is integer other wise crash the exception and not work and error show form.
    # else only work for try not work for exceot