# creating Thread using a Class

from threading import *
from time import * # just to see printing a little bit slower

def display_chars(msg):
    l.acquire() #locks so that first task finishes before second one starts. Otherwise the printed message will be mixed up
    for i in msg:
        print(i)

    l.release() # unlock. now another task can start to avoid mixing up the message while printing

l = Lock()
t1 = Thread(target=display_chars, args=("HELLO WORLD",)) # args takes only one argument so we pass it as tuple
t2 = Thread(target=display_chars, args=("you are welcome",)) #target is a function that doesnt allow parameters. this can be overcome by target=lambda:display_chars(param) if needed

t1.start()
t2.start()

t1.join()
t2.join()