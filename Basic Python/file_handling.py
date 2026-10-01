#method reading
f = open ("data.txt","r")
f.read()
f.close()

#method writing
f = open ("data.txt","w")
f.write(b"Hello how are you")
f.close()

#method append
f = open ("data.txt","a")
f.write(b"Hello how are you")
f.close()