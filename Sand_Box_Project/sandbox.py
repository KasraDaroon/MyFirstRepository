class BankAccount:
 
    account_counter = 1 
    
    def __init__(self, name, accountType, balance=0):
        
        self.name = name
        self.accountType = accountType
        self.balance = balance
        
        self.accountNumber = BankAccount.account_counter
        BankAccount.account_counter += 1
              
        self.filename = str(self.accountNumber) + "_" + self.accountType + "_" + self.name + ".txt"
        
        with open(self.filename, 'w') as file:
            file.write(f"Account Number: {self.accountNumber}\n")
            file.write(f"Account Type: {self.accountType}\n")
            file.write(f"Account Holder: {self.name}\n")
            file.write(f"Initial Balance: ${self.balance}\n")
            file.write("Transactions:\n")

    def deposit(self, amount):
        self.balance += amount
        self._update_transaction("Deposit", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self._update_transaction("Withdrawal", amount)
        else:
            print("Insufficient funds!")

    def get_user_id(self):
        return self.accountNumber

    def get_username(self):
        return self.name

    def get_account_type(self):
        return self.accountType

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def _update_transaction(self, transaction_type, amount):
        with open(self.filename, 'a') as file:
            file.write(f"{transaction_type}: ${amount}\n")
            file.write(f"Current Balance: ${self.balance}\n")
