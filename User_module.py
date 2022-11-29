# class user:
#
#     def __init__(self,fname,lname,age,location):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#         self.location = location
#
#     def describe_user(self):
#         print(f"\nHi my name is {self.fname} {self.lname}")
#         print(f"I am {self.age} years old")
#         print(f'I stay in {self.location}')
#
#     def greet_user(self):
#         print(f"Hello {self.fname} {self.lname}. Welcome..!!")

# class admin(user):
#
#     def __init__(self,fname,lname,age,location):
#         super().__init__(fname,lname,age,location)
#         self.privilege = Privilege()
# class Privilege:
#     def show_privileges(self):
#         privileges = ['can add post','can delete post','can ban user']
#         print("\nThe admin privilages are: ")
#         for privilege in privileges:
#             print(f"{privilege}".title())

