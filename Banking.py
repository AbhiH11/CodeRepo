# 1.Create account contains name and account number
# 2.show account
# 3.Deposit amount
# 4.withdraw amount
# 5. show balance
# 6.choice(menu)
# 7.Quit

class user:

    def __init__(self,name,age,gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details: ")
        print("Name:", self.name)
        print('Age:', self.age)
        print('Gender:', self.gender)

class bank(user):

    def __init__(self, name, age, gender) -> None:
        super().__init__(name, age, gender)
        self.balance = 0
        self.amount = 0
    
    def deposit_amount(self):
        self.amount = int(input("Enter the amount you want to deposit: "))
        self.balance = self.amount + self.balance
        print(f" Your Accoount balance is updated:", self.balance)

    def withdraw_amount(self):
        self.amount = int(input("Enter the amount you want to withdraw: "))
        if self.amount > self.balance:
            print(f'You have insufficient funds', self.balance)
        else:    
            self.balance = self.balance - self.amount
            print(f'Your balance is updated:', self.balance)
    
    def view_balance(self):
        self.show_details()
        print(f"Your account balance is:", self.balance)

# c= bank("Abhi",30,'Male')
# c.deposit_amount(300)
# c.withdraw_amount(200)
if __name__ == '__main__':
    c = bank("Abhi",30,'Male')

# """MENU = (1.Show details;
# 2.Deposit amount;
# 3.Withdraw amount;
# 4. View balance
# 5.Quit)"""

    while True:
        choice = int(input("Enter your option: "))

        if choice == 1:
            c.show_details()
        if choice == 2:
            c.deposit_amount()
        if choice == 3:
            c.withdraw_amount()
        if choice == 4:
            c.view_balance()
        if choice == 5:
            break
