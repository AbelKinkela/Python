class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def multiplication(a, b):
        return a * b
    @staticmethod
    def subtraction(a, b):
        return a - b
    @staticmethod
    def division(a, b):
        return a / b
    

if __name__ == "__main__":
    x = 10
    y = 2
    print("x:",x, "y: ", y )
    print("Addition:",Calculator.add(x, y))
    print("Subtraction:",Calculator.subtraction(x, y))
    print("Multiplication:",Calculator.multiplication(x, y))
    print("Division:",Calculator.division(x, y))