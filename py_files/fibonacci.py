'''fibonacci is implemented in 2 ways below.
1) using recursive method
2) using while loop'''
# 1). Recursive method:
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = 10
result = [fibonacci(i) for i in range(n)]
print(result)

#2) While loop:

def fibonacci(n):
    a,b = 0,1
    while a < n:
        print (a)
        a,b = b, a + b
        # return a, b

for i in fibonacci(20):
    print(i)        
# n = 10
# result = [fibonacci(i) for i in range(n)]
# print(result)