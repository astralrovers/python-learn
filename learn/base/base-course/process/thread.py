from threading import Thread, enumerate
from time import ctime, sleep

import os

num = 0

def print_time1(name):
    roll = 3
    while roll > 0:
        print('......%s.....%s....'%(name, ctime()))
        roll -= 1
        global num
        num += 1
        sleep(3)
        print('thread1 num : %d'%num)

def print_time2(name):
    roll = 3
    while roll > 0:
        print('......%s.....%s....'%(name, ctime()))
        roll -= 1
        global num
        num += 1
        sleep(3)
        print('thread2 num : %d'%num)

p1 = Thread(target=print_time1, args=('centos',))
p2 = Thread(target=print_time2, args=('ubuntu',))
p2.start()
p1.start()

print(len(enumerate()))
print('end')
#wait child thread exit
