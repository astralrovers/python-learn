from ctypes import *

adder = CDLL('./adder.so')


print adder.py_add(4, 5)
