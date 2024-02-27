# creating Thread using a function

from threading import *
from time import * # just to see printing a little bit slower


def display():
    for i in range(65, 91):
        print(chr(i))
        sleep(1)


t = Thread(target=display, name='Alphabets') # creates a thread that will run the display function
t.start() # call to run the thread

for i in range(65, 91):
    print(i)
    sleep(1)

t.join() # main part of program (the for loop that prints numbers) will wait the t thread to finish