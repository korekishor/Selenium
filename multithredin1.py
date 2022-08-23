"""import threading

import time

class paintwall:

    def paint(self):
        time.sleep(2)
        print("wall painted")

    def __init__(self):
        t=threading.Thread(target=self.paint())
        t.start()

paintwall()
paintwall()
paintwall()
paintwall()
"""
"""from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))



"""

"""
from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
"""
"""
from concurrent.futures import thread
from threading import *

def display():
    for i in range(10):
        print("chield thread")

t=Thread(target=display)
t.start()

for i in range(10):
    print("main thread")
"""
"""
from threading import *

class Mythread(Thread):
    def run(self):
        for i in range(10):
            print("chield thread")

t=Mythread()
t.start()

for i in range(10):
    print("main thread")

"""

# without using any class 
# by extending thread class 
#  without extending thread class

"""
from threading import Thread
class testing:
    def m1(self):
        for i in range(10):
            print("chield thread")

obj=testing()
t=Thread(target=obj.m1)
t.start()

for i in range(10):
    print("main thread")

"""

"""
from threading import Thread
import time

def double(number):
    for i in (number):
        time.sleep(1)
        print("double value :" ,2*i)

def square(number):
    for n in number:
        time.sleep(1)
        print("square of number : ",n*n)

number=[1,2,3,4,5]
begiintime=time.time()

t1=Thread(target=double,args=(number,))
t2=Thread(target=square,args=(number,))
t1.start()
t2.start()

t1.join()
t2.join()

# double(number)
# square(number)
endtime=time.time()

print("total time taken by ",endtime-begiintime)
"""

from threading import *

print(current_thread().getName())
current_thread().setName("new_name_thread")

current_thread().name="new1_name"
print(current_thread().getName())
print(current_thread().ident)
print(active_count())
