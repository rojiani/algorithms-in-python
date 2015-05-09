
# Greedy Activity Selection - Recursive
# a = {a_1, a_2, ..., a_n} - set of activities
# each a_i has a start time s_i and finish time f_i -> 0 <= s_i <= f_i
# 2 activities a_i & a_j, i != j, are compatible if f_i <= s_i or f_j <= s_i
# Select the largest set of mutually compatible activities 


def recursive_activity_selector(a, A, m, k):    
    if m == 1:          # first call: select first activity
        A.append(a[0])
    if m == len(a):     # base case
        return A
    else:   
        if a[m][0] >= a[k][1]:
            A.append(a[m])
            k = m
        return recursive_activity_selector(a, A, m + 1, k)

def driver():
    # a_i = (s_i, f_i)
    a = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), 
         (8, 12), (2, 14), (12, 16)]
    solution = recursive_activity_selector(a, [], 1, 0)
    print("SOLUTION: " + str(solution))

# book version
"""
def recursive_activity_selector(a, A, k):
    n = len(a)
    # first call only - set up
    if k == 0:
        A.append(a[0])
    m = k + 1
    while m < n and a[m][0] < a[k][1]:   # find the 1st activity in S_k to finish
        m = m + 1
    if m < n:       
        A.append(a[m])
        return recursive_activity_selector(a, A, m)
    else:
        return A


def driver():
    # a_i = (s_i, f_i)
    a = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), 
         (8, 12), (2, 14), (12, 16)]
    solution = recursive_activity_selector(a, [], 0)
    print("SOLUTION: " + str(solution))
"""

driver()