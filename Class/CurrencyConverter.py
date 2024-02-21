
class CurrencyConverter:

    def __init__(self, name, rate) -> None:
        self.name = name
        self.rate = rate

    def set_name(self, name):
        self.rate = name

    def set_rate(self, rate):
        self.rate = rate
    
    def get_rate(self):
        return self.rate

    def convert(self, amount):
        return amount * self.rate
    

if __name__ == "__main__":

    kwanza_to_usd = CurrencyConverter('AOA', 832.50)
    congo_franc_to_usd = CurrencyConverter('FC', 2750)


    print(f'100 Kwanza = {kwanza_to_usd.convert(100):.2f}')
    print(f'100 FC = {congo_franc_to_usd.convert(100):.2f}')