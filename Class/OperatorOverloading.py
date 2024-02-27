# The goal of this exercise is to practice about Operator Overloading
class Rational(object):
    def __init__(self, p=1, q=1) -> None:
        self.p =p
        self.q=q

    def __str__(self) -> str:
        return f'{self.p}/{self.q}'

    def __mul__(self, other):
        return Rational(self.p* other.p,  self.q*other.q)

    def __add__(self, other):
        return Rational(self.p* other.q + self.q*other.p, self.q*other.q)
    
    def __sub__(self, other):
        return Rational(self.p* other.q - self.q*other.p, self.q*other.q)

if __name__ == "__main__":  
    r1 = Rational(2, 4)
    r2 = Rational(3, 6)


    sum = r1 + r2
    print(sum) # prints 24/24
    sub = r1 - r2
    print(sub) # prints 0/24
    mult = r1 * r2
    print(mult) # prints 6/24