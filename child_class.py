class Parent:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def partial(self):
        print(self.fname, self.lname)

class Child(Parent):
    def __init__(self, fname, lname, year):
        super().__init__(fname,lname)
        self.grad_year = year
    def welcome(self):
        print("welcome", self.fname,self.lname, "to the class of",self.grad_year)
z =Child("abhi", "hari", 2010)
z.welcome()
