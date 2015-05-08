"""
Fibonacci dynamic programming - top-down (memoization) approach
# http://www.algorithmist.com/index.php/Dynamic_Programming

Using a decorator

"""

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize   # not strictly necessary
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci = memoize(fibonacci)      # decorator

print("Testing")
tests = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), \
         (8, 21), (9, 34), (10, 55), (25, 75025), (50, 12586269025), \
         (100, 354224848179261915075), \
         (200, 280571172992510140037611932413038677189525),
         (300, 222232244629420445529739893461909967206666939096499764990979600)]         
for test in tests:
    result = fibonacci(test[0])
    if result == test[1]:
        print("PASS: %d" % result)
    else:
        print("FAIL: %d" % result)


# import timeit
# p=300
# print("fibonacci (decorator)")
# print("%.8f" % (timeit.timeit("fibonacci(p)", setup = "from __main__ import fibonacci, p", number=1)))
