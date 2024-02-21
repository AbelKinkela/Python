from math import pi


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius
    
    def area(self):
        return pi * self.radius**2
    

if __name__ == "__main__":
    c1 = Circle(7)
    print(f'Area: {c1.area():.2f}')
    print(f'Perimeter: {c1.perimeter():.2f}')