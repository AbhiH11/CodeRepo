# def palindrome(word):
#     return word == word[::-1]

# n  = input("Enter a word to check for Palindrome: \n")
# if palindrome(n):
#     print(f'The word {n} is a palindrome')
# else:
#     print(f"The word {n} is not a palindrome")


def palindrome(n):
    return n == n[::-1]

n = input("Enter a word to check if its a palindrome: \n")

if palindrome(n):
    print(f"The word {n} is a palindrome")
else:
    print(f"The word {n} is not a palindrome")
