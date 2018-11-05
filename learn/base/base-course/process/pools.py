from multiprocessing import Pool, Manager
import os
import time

def print_name(name, lock):
    time.sleep(1)
    print('into')
    with lock:
        print('...%s...%d.....'%(name, os.getpid()))
        time.sleep(2)


lock = Manager().Lock()

p = Pool(3)

for i in range(0, 9):
    #Pool.apply_async(要调用的目标,(传递给目标的参数元祖,))
    #每次循环将会用空闲出来的子进程去调用目标
    p.apply_async(print_name, ('centos', lock))

print('start')
#关闭进程池，关闭后po不再接收新的请求
p.close()
p.join()

print('end')
