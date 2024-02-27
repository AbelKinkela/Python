from threading import *
from time import * # just to see printing a little bit slower

class Table:
    def __init__(self) -> None:
        self.food = ""
        self.flag = False
        #self.lock = Lock() if need can be added here
    
    def put_food(self, food):
        while self.flag != False:
            pass
        #self.lock.aquire()
        self.food = food
        print("I put", self.food)
        self.flag = True
        #self.lock.release()
    def eat_food(self):
        while self.flag != True:
            pass
        print("I eat", self.food)
        self.flag = False


obj = Table()


food = iter(["Rice and Chicken", "Fruits", "Kebab", "Cake","Rice and Chicken", "Fruits", "Kebab", "Cake","Rice and Chicken", "Fruits", "Kebab", "Cake"])
    
def producer():
    n = 0
    while n < 12:
        obj.put_food(next(food))
        n += 1
        
def consumer():
    n = 0
    while n < 12:
        obj.eat_food()
        n += 1

t1 = Thread(target=producer) #target is a function that doesnt allow parameters. this can be overcome by target=lambda:poducer(param)
t2 = Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()