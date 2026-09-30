#Read mode for binary file
f = open("sample.bin","r")
f.read()
f.close()

#Write mode for binary file
f = open("grow.bin","bw")
f.write(b"Hello World")
f.close()

#append mode for binary file
f = open("grow.bin","ba")
f.write(b"what is your name")
f.close()