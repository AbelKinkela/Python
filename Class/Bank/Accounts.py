
from Account import Account
import RulesAndExceptions as RE

try:
    accounts = {
        'abel': Account("Abel Kinkela", "Premium", 50),
        'fatima': Account("Fatima Cainda", "Basic", 4000),
        'costa': Account("Costa Cainda", "Medium", 501),
        'teresa': Account("Teresa Kinkela", "Medium", 2345)
    }
except RE.AccountBalanceException as e:
    print(e)