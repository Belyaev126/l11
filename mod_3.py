#!/usr/bin/env python3
# -*- config: utf-8 -*-


def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


if __name__ == '__main__':
    import timeit

    print(timeit.timeit("factorial(10)", setup="from __main__ import factorial"))
    print(timeit.timeit("fib(10)", setup="from __main__ import fib"))