"""
Fibonacci dynamic programming - top-down (memoization) approach

Using Python's 'memo' decorator

Other ways to implement memoization in Python: see Mastering Object-Oriented
Python, p. 150 (lru_cache)
"""

def fibonacci(n):           # driver
    return fib(n, {})

def fib(n, memo= {}):
    if n == 0 or n == 1:
        return n
    try:
        return memo[n]
    except KeyError:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]


print("Testing")
tests = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), \
         (8, 21), (9, 34), (10, 55), (25, 75025), (50, 12586269025), \
         (100, 354224848179261915075)]
for test in tests:
    result = fibonacci(test[0])
    if result == test[1]:
        print("PASS: %d" % result)
    else:
        print("FAIL: %d" % result)

import timeit
p=300
print("fibonacci (bottom-up)")
print("%.8f" % (timeit.timeit("fibonacci(p)", setup = "from __main__ import fibonacci, p", number=1)))
