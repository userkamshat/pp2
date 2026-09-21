class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Not enough money")

    def show_balance(self):
        print("Balance:", self.balance)


account = Account("KBTU", 1000)

account.deposit(500)
account.withdraw(300)
account.withdraw(1500)

account.show_balance()