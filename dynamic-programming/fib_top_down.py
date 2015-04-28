# Fibonacci dynamic programming - top-down (memoization) approach
# http://www.algorithmist.com/index.php/Dynamic_Programming
# How to memoize with python (global array issues?):
#   http://www.python-course.eu/python3_memoization.php
# Alternative python version using memoization as decorator:
#   https://technobeans.wordpress.com/2012/04/16/5-ways-of-fibonacci-in-python/

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib = memoize(fib)


print("TESTS")
tests = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), \
        (8, 21), (9, 34), (10, 55), (25, 75025), (50, 12586269025), \
         (100, 354224848179261915075)]
for test in tests:
    result = fib(test[0])
    if result == test[1]:
        print("PASS: %d" % result)
    else:
        print("FAIL: %d" % result)