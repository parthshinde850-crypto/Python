f = open("file.txt")#automatically in read mode
lines = f.readlines()
print(lines, type(lines))
f.close()   # save the file otherwise [] output give (command +s)