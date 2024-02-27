# creating Thread using a Class

from threading import *
from time import * # just to see printing a little bit slower

class Alphabets(Thread): 
    def run(self):
        for i in range(65, 91):
            print(chr(i))
            sleep(1)


t = Alphabets() # that's all its needed after we have inherited from Thread and overiden the run(self) method
t.start() # call to run the thread

for i in range(65, 91):
    print(i)
    sleep(1)

t.join() # main part of program will wait the t thread to finish