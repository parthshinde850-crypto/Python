with open("poem.txt") as f:
    read = f.read()

    if ("twinkle" in f):
        print("yes ")
    else:
        print("no")