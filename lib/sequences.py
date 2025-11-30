#!/usr/bin/env python3


def print_fibonacci(length):
    if length == 0:
        print([])
        return
    fib = [0]
    if length == 1:
        print(fib)
        return
    fib.append(1)
    if length == 2:
        print(fib)
        return
    for i in range(2, length):
        fib.append(fib[-1] + fib[-2])
    print(fib)
