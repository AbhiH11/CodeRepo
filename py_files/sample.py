z = input("enter title: ")
d = input ("enter a message: ")

b = z + ".txt"
f = open(b, "w")
f.write(d)
#f.close()
