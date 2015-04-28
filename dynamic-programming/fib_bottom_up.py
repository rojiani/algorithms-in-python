# Fibonacci dynamic programming - bottom-up approach
# http://www.algorithmist.com/index.php/Dynamic_Programming


def fibonacci(n):
    table = [None] * (n+2)  # n+1 so no error if n=0
    
    # fill up table
    table[0] = 0
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i-1] + table[i-2]
    return table[n]


print("TESTS")
tests = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), \
        (8, 21), (9, 34), (10, 55), (25, 75025), (50, 12586269025), \
         (100, 354224848179261915075)]
for test in tests:
    result = fibonacci(test[0])
    if result == test[1]:
        print("PASS: %d" % result)
    else:
        print("FAIL: %d" % result)