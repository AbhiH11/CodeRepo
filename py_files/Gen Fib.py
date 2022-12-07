def fib(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b, a + b
x = fib(5)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())


print("\n using  for in loop")
for i in fib(5):
    print(i)
