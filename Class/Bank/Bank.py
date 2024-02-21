import pickle
import Accounts as Accounts
from Account import Account
import RulesAndExceptions as RE

def decorator(f):
    def wrapper(msg):
        print("*" * 30)
        f(msg)
    return wrapper

def display(msg):
    print(msg)

d = decorator(display)

if __name__ == "__main__":
    accounts = Accounts.accounts

    # Deposit 500 in all accounts
    for account in accounts.values():
        deposit_response = account.deposit(500)
        d(deposit_response)

    

