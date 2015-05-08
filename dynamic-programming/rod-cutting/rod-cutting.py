"""
Rod-Cutting Problem
Dynamic Programming
CLRS 15.1
"""
# value of uncut rods
uncut = {
    #length: price
     0:  0,
     1:  1,
     2:  5,
     3:  8,
     4:  9,
     5: 10,
     6: 17,
     7: 17,
     8: 20,
     9: 24,
    10: 30
}

# length: max price from cutting
optimal = { 0:0, 1:1 }

def cut_rod(n):
    if n < 0 or n > 10:
        print("Input error: n must be in range [0, 10]")
        return
    result = find_optimal(n)
    print("Max. value for length %d is %d" % (n, result))
    return result

# Find optimal price for length n
def find_optimal(n):
    max_value = uncut[n]
    for cut in range(1, int(n/2) + 1):
        left_value = optimal[cut] if cut in optimal else find_optimal(cut)
        right_value = optimal[n-cut] if (n-cut) in optimal else find_optimal(n-cut)
        max_value = max(max_value, left_value + right_value)
    optimal[n] = max_value
    return optimal[n]

print("Optimal values for rods of length 1-10")
for n in range(1, 10+1):
    cut_rod(n)

