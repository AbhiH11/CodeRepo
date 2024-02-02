a = int(input("Enter a number: "))
print("Multiplication of a is: ")
try:
    for i in range(1,11):
        print(f"{a} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
finally:
    print("\nI will always execute no matter what ..!")

print("Multiplication output")
print("The End")
