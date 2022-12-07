class theatre:
    def __init__(self, Persons, Amount):
        self.Persons = Persons
        self.Amount = Amount

    def call(self):
        print(self.Persons, self.Amount)


class Parking(theatre):
    def __init__(self, Persons, Amount, Status):
        super().__init__(Persons, Amount)
        self.Status = Status

    def message(self):
        print("No. of people entered: ", self.Persons, "\nPaid amount:", self.Amount, "\nStatus: ", self.Status)


allow = Parking(2, 200, "Enter")
allow.message()
