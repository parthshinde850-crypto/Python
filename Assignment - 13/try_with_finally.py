def main():
    try :
        a = int(input("Enter a number:"))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally: #finally work for both try and except and we did nt use print instead of finally because when we use in def it didnt print the "print"
        print("I am inside else!")

main()