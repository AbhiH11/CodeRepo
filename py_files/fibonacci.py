'''fibonacci is implemented in 2 ways below.
1) using recursive method
2) using while loop'''

import time
# 1). Recursive method:
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = 10
# init = time.time()
result = [fibonacci(i) for i in range(n)]
print(result)
# print(f"Using Recursion it took {time.time() - init}")
#2) While loop:

# def fibonacci(n):
#     a,b = 0,1
#     if a ==1:
#         print(a)
#         # print(b)
#     else:
#         print(a)
#         print(b)
#         for i in range (2,n):
#             c = a + b
#             a = b
#             b = c
            
#             print(c)

# fibonacci(10)
init = time.time()
print(f'It took {time.time() - init} seconds')