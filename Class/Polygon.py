from abc import ABC, abstractmethod
from math import sqrt

class Polygon(ABC):
    def __init__(self, no_of_sides, *sides) -> None:
        self.no_of_sides = no_of_sides
        self.sides = sides
    
    @abstractmethod
    def area(self) -> float:
        pass

class Triangle(Polygon):
    def __init__(self, no_of_sides, *sides) -> None:
        super().__init__(no_of_sides, *sides)
    
    def area(self) -> float:
        s = sum(self.sides)/2
        return sqrt(s* (s-self.sides[0]) * (s - self.sides[1]) * (s-self.sides[2]))
    

if __name__ == "__main__":
    t1 = Triangle(3, 10, 15,9)
    print(t1.area())