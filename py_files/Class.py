# class abhi():
#   def __init__(self, name, age):
#      self.name = name
#     self.age = age

# p1 = abhi("hari",29)
# print(p1.name)
# print(p1.age)

# class computer():
# def __init__(self, name, gen):
#   self.name = name
#    self.gen = gen
# def my_object(ads):
#      print("The computer name is " + ads.name)
#       print("The gen is " + ads.gen)

# specifics = computer("dell","ten")
# print(specifics.name)
# print(specifics.gen)
# specifics.my_object()


# class market():
# def __init__(self,price, quantity):
#   self.price = price
#    self.quantity = quantity

# def order(self):
#      print("The price is :\n" + self.price)
#       print("the quantity is :\n" + self.quantity)

# z = market("ten","five")
# z.price = "twenty"
# del z.price
# del z
# z.order()


class random:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


class qwerty(random):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.grad_year = year

    def welcome(self):
        print("welcome", self.fname, self.lname, "to the batch of", self.grad_year)


d = qwerty("abhi", "hari", 2010)
d.welcome()
