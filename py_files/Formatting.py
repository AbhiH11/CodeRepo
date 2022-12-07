x = input("Enter a name :")
y = input("Im from: ")
z = int(input("my age is : "))
#print(f"my name is {x}")
#w = "my name is {}, im from {}, my age is {}"
#print(f"my name is {x}, im from {y}, my age is {z}")
op = "my name is {}, im from {}, my age is {}"
print(op.format(x,y,z))