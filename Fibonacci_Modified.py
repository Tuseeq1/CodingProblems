"""
Hacker Rank Problem
Name: Fibonacci Modified
link: https://www.hackerrank.com/challenges/fibonacci-modified/problem

solution:
"""


def fibonacci_modified(t1, t2, n):
    return find_fibonacci(t1, t2, n, 3)


def find_fibonacci(t1, t2, n, x):
    # find for the xth number starting from 3 and return if x==n
    tx = t1 + (t2 * t2)
    if x == n:
        return tx
    return find_fibonacci(t2, tx, n, x + 1)
