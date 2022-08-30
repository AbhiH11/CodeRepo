from collections import deque

a = deque([3,8,9,7,6])

def fun(a,n):
    k = 1
    n = 1
    while True:
        a.rotate(n)
        print(list(a))
        k += 1

        if k == 4:
            return

fun(a,n=1)
