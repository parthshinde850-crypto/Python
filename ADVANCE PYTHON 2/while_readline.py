f = open("file.txt")

line = f.readline()
while(line != ""):#not equal to it so it print the lines 
    print(line)
    line = f.readline()#not use then output continously print it not stop 

f.close()