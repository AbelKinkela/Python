from threading import *
from time import * # just to see printing a little bit slower
from queue import Queue


my_queue = Queue()

food = iter(["Rice and Chicken", "Fruits", "Kebab", "Cake","Rice and Chicken", "Fruits", "Kebab", "Cake","Rice and Chicken", "Fruits", "Kebab", "Cake"])
    
def producer():
    n = 0
    while n < 12:
        f = next(food)
        print("Puting", f)
        my_queue.put(f)
        n += 1
        
def consumer():
    n = 0
    while n < 12:
        print("Eating", my_queue.get())
        n += 1

t1 = Thread(target=producer) #target is a function that doesnt allow parameters. this can be overcome by target=lambda:poducer(param)
t2 = Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()