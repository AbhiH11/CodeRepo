# a = input("Enter a sequence: ")
# b = a[::-1]
#
# if a == b:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


def func(r):
    for i in range(r):
        print(' '*(r-i-1)+'*'*(2*i+1))
func(6)