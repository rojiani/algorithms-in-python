"""
Fibonacci dynamic programming - top-down (memoization) approach

Using a dictionary for memoization
"""

# Use a dictionary to store previously calculated values
memo = { 0:0, 1:1 }
def fibo_dict(n):
    if not n in memo:
        memo[n] = fibo_dict(n-1) + fibo_dict(n-2)
    return memo[n]

# Use a list instead of dictionary - about the same efficiency as dictionary,
# maybe faster for n > 100?
memo_lst = [0, 1] + [None] * (1000-2)
def fibo_list(n):
    if memo_lst[n] is None:
        memo_lst[n] = fibo_list(n-1) + fibo_list(n-2)
    return memo_lst[n]

print("Testing fibo_dict")
tests = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), \
         (8, 21), (9, 34), (10, 55), (25, 75025), (50, 12586269025), \
         (100, 354224848179261915075), \
         (200, 280571172992510140037611932413038677189525),
         (300, 222232244629420445529739893461909967206666939096499764990979600)]         
for test in tests:
    result = fibo_dict(test[0])
    if result == test[1]:
        print("PASS: %d" % result)
    else:
        print("FAIL: %d" % result)


print("Testing fibo_list")
tests = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), \
         (8, 21), (9, 34), (10, 55), (25, 75025), (50, 12586269025), \
         (100, 354224848179261915075), \
         (200, 280571172992510140037611932413038677189525),
         (300, 222232244629420445529739893461909967206666939096499764990979600)]         
for test in tests:
    result = fibo_list(test[0])
    if result == test[1]:
        print("PASS: %d" % result)
    else:
        print("FAIL: %d" % result)


# import timeit
# p=300
# print("dict")
# print("%.8f" % (timeit.timeit("fibo_dict(p)", setup = "from __main__ import fibo_dict, p", number=1)))
# print("list")
# print("%.8f" % (timeit.timeit("fibo_list(p)", setup = "from __main__ import fibo_list, p", number=1)))

