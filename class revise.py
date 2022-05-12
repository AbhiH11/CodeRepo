# # name = input("Enter a name: ")
# # age = input("Enter a age: ")
# class hall:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#
# class person(hall):
#     def __init__(self,name,age,country):
#         super().__init__(name, age)
#         self.country = country
#
#     def message(self):
#         print("Welcome", self.name, self.age, self.country)
#
# z = person("Abhi", 29,"Ind")
# z.message()



class zoo:
    def __init__(self,animals,loc):
        self.animals = animals
        self.loc = loc


class branch(zoo):
    def __init__(self,animals,loc,status):
        super().__init__(animals,loc)
        self.status = status

    def message(self):
        print("All",self.animals,"animals", "from",self.loc,"Zoo", "are",self.status)

x = branch(32,"Hyd","Healthy")
x.message()