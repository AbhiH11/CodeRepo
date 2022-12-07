class School:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def grade(self):
        print(self.name, self.age)


class Subject(School):
    def __init__(self, name, age, lists):
        super().__init__(name, age)
        self.lists = lists

    def Student_details(self):
        print("Student details are: ", "\nname: ", self.name, "\nage: ", self.age, "\nand subject chosen: ",
              self.lists)


det = Subject("Abhi", 29, "Eng, Italian, Sanskrit")
det.Student_details()
