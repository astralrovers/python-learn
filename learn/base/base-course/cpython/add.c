#include <stdio.h>

int py_add(int prev, int next)
{
	return prev + next;
}
#gcc -shared -Wl,-soname,adder -o adder.so -fPIC add.c
