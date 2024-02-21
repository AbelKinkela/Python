
import random


class Dice:
    def __init__(self, sides=6) -> None:
        self.sides = sides
    
    def roll_dice(self):
        return random.randint(1,self.sides)


d1 = Dice()
outcome = d1.roll_dice()
print(outcome)