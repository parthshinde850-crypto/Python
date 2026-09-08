with open ("poem.txt") as f:
    content = f.read()

if "twinkle" in content.lower():
    print("yes")
else:
    print("no")