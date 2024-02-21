import RulesAndExceptions as RE

class Account:
    account_number = 1001
    def __init__(self, name, cat, balance) -> None:
        if balance < RE.CURR_MIN_ALLOW_BAL:
            raise RE.AccountBalanceException("Error: Balance is below minimum allowed threshold")
        self.number = Account.account_number
        self.name = name
        self.cat = cat
        self.balance = balance
        Account.account_number += 1

    def __str__(self):
        return f"Account: {self.number}\nName:{self.name}\nCategory: {self.cat}\nBalance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return "Amount successfully deposited\n"+ "Current Balance: "+ str(self.balance)


    def withdraw(self,amount):
        if (self.balance - amount) < RE.CURR_MIN_ALLOW_BAL:
            raise RE.AccountBalanceException(f"Error: Trying to withdraw more than allowed. Allowed: {self.balance - RE.CURR_MIN_ALLOW_BAL}")
        else:
            inital_bal = self.balance
            self.balance -= amount
            print(self.balance)
            return f"Initial balance: {inital_bal:.2f}\nAmount withdrawn: {amount:.2f}\nRemaining Balance:{self.balance:.2f}"
