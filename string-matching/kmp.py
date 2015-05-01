# Returns list contains the valid shifts instead of printing them.
def kmp_matcher(T,P):
    n = len(T)
    m = len(P)
    pi = compute_prefix_function(P)     
    q = 0                               # number of characters matched
    shifts = []                         # stores valid shifts, if any
    for i in range(n):                  # shifted bounds [1...n] to [0...n-1]
        while q > 0 and P[q] != T[i]:
            q = pi[q-1]                 # next character does not match
        if P[q] == T[i]:
            q += 1
        if q == m:
            shifts.append(i - m + 1)
            q = pi[q-1]
    return shifts

def compute_prefix_function(P):
    m = len(P)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = pi[k-1]
        if P[k] == P[q]:
            k += 1
        pi[q] = k
    return pi

def solve_HW10_Problem2():
    pattern = 'ababbabbabbababbabb';
    expected = [0, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 7, 8]
    print("pi[1...m] for pattern 'ababbabbabbababbabb' is:")
    print(compute_prefix_function(pattern), expected)

solve_HW10_Problem2()

"""
Output:
pi[1...m] for pattern 'ababbabbabbababbabb' is:
[0, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 7, 8] [0, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
[Finished in 0.0s]
"""