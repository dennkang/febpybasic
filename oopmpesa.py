from abc import ABC, abstractmethod

# Encapsulation
class Account:

    # constructor method
    def __init__(self, account_id, holder_name, balance):
        self.account_id = account_id
        self.holder_name = holder_name
        self.balance = balance

    # method function
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")

        else:
            print("Insufficient funds to withdraw")

    def get_balance(self):
        return self.balance

    def get_holder(self):
        return self.holder_name

# inheritance
class Customer(Account):
    def __init__(self, account_id, holder_name, balance, phone_number):
        super().__init__(account_id, holder_name, balance)
        self.phone_number = phone_number

# polymorphism
class Transaction:
    def __init__(self, amount):
        self.amount = amount

    def execute(self, account):
        pass

class Deposit_Transaction(Transaction):
    def execute(self, account):
        account.deposit(self.amount)

class Withdraw_Transaction(Transaction):
    def execute(self, account):
        account.withdraw(self.amount)

# abstraction
class Payment_System(ABC):
    @abstractmethod

    def process_transaction(self, amount):
        pass

class MyPaymentSystem(Payment_System):
    def process_transaction(self, amount):
        print(f"Transaction Processing of {amount}")

mpesa = MyPaymentSystem()
account1 = Customer(1,"John", 1000, 25472)

deposit = Deposit_Transaction(500)
withdraw = Withdraw_Transaction(800)
deposit2 = Deposit_Transaction(2000)

deposit.execute(account1)
withdraw.execute(account1)
deposit2.execute(account1)

print(f"Balance for {account1.get_holder()} is {account1.get_balance()}")