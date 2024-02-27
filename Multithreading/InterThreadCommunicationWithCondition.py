from threading import *
from time import * # just to see printing a little bit slower

class Table:
    def __init__(self) -> None:
        self.food = ""
        self.cond = Condition()
    
    def put_food(self, food):
        self.cond.acquire() # state the desire to aquire 
        self.cond.wait(timeout=0) # no timeout, imediately start 
        self.food = food
        print("I put", self.food)
        self.cond.notify()
        self.cond.release()

    def eat_food(self):
        self.cond.acquire() # state the desire to aquire 
        self.cond.wait(timeout=0) # no timeout, imediately start 
        print("I eat", self.food)
        self.cond.release()
        self.cond.notify()


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