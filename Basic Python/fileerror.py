filename = input("Enter filename to open: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n", content)

except FileNotFoundError:
    print("Error: File not found! Please check the filename.")