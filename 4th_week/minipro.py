#Mini Project:
#-Create a simple banking system with classes for `Bank`, 
#`Account`, and `Customer`. Implement functionalities like creating a new account, 
#view details of existing accounts, withdraw and deposit money, 
#and transfer money between accounts. Ensure proper exception handling for scenarios
# like insufficient funds or invalid account operations.

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def get_account(self, account_number):
        account = self.accounts.get(account_number)
        if account is None:
            raise ValueError(f"Account {account_number} does not exist")
        account.get_details()

    def create_account(self, customer, initial_amount):
        account = Account(customer, initial_amount)
        # {1001: <account_object>, .....}
        self.accounts[account.account_number] = account
        return account
    
 
class Account:
    account_number = 1000

    def __init__(self, customer, initial_amount):
        self.customer = customer
        self.balance = initial_amount
        Account.account_number += 1
        self.account_number = Account.account_number

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient funds.")

        self.balance -= amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount

    def get_details(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Customer Name:", self.customer.name)
        print("Address:", self.customer.address)


class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address


bank = Bank("BIA")

customer1 = Customer("abhi", "hyd")
customer2 = Customer("Gayatri", "hyd")
customer3 = Customer("Ramya", "hyd")


account1 = bank.create_account(customer1, 100)
account2 = bank.create_account(customer2, 100)
account3 = bank.create_account(customer3, 300)







print(account1.deposit(500))
print(account1.withdraw(100))

bank.get_account(1001)

