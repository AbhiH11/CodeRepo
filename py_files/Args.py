# def my_name(*name):
#     # self.fname = fname
#     # self.lname = lname
#     # print("my name is",self.fname, self.lname)
#     print("My name is\n" +name[0])
#
# my_name("Abhi","Hari","Anu")




def my_name(**name):
    print("My name is",name["fname"],name["lname"])
my_name(fname="Abhi",lname = "Hari")


