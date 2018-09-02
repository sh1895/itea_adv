
# coding: utf-8

import math
from math import gcd as nod

def fac(n):
    arg = math.factorial(n)
    return(arg)


def gcd(a, b):
    c = nod(a, b)
    """
    while a!=0 and b!=0:
        if a > b:
            a = a % b
        else:
            b = b % a
        c = a + b
    """
    return(c)


def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
    


for number in fib():
    if number > 100:
        break
    print (number)



def flatten(seq):
    for i, item in enumerate(seq): 
        if hasattr(item, '__iter__'): 
            for nested in flatten(item): 
                yield nested 
        else: 
            yield item 




def call_count():
    """
    Декоратор, подсчитывающий количество вызовов задекорированной функции.

    Пример использования:

    @call_count
    def add(a, b):
        return a + b

    >>> add.call_count
    0
    >>> add(1, 2)
    3
    >>> add.call_count
    1

    Подсказки по реализации: функторы, @property

    """
    pass

