'''Using "Else" with the for/while loop:
Else statement executes only after the for/while loop is executed.
Else statement is printing out doesnt mean that the for loop breaks'''

# for i in range(10):
#     print(i)
#     if i == 5:
#         break
# else:
#     print("sorry no i")

i = 1
while i < 8:
    print(i)
    i +=1
    if i == 4:
        break
else:
    print("End of loop")