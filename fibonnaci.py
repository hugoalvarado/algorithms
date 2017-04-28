from functools import lru_cache
from timeit import timeit

# f(0) = 0 f(1)=1

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def fib_nr(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
	
	
@lru_cache(maxsize=None)
def fib_r(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)   