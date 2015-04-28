# Greedy Activity Selection
# a = {a_1, a_2, ..., a_n} - set of activities
# each a_i has a start time s_i and finish time f_i -> 0 <= s_i <= f_i
# 2 activities a_i & a_j, i != j, are compatible if f_i <= s_i or f_j <= s_i
# Select the largest set of mutually compatible activities 

def greedy_activity_selector(a):
    n = len(a)
    # Sort by increasing f_i
    a.sort(key=lambda x: x[1])

    """Greedily select activities by going down the list and by picking 
       whatever activity that is compatible with the current selection"""
    A = [a[0]]
    k = 0   # current activity idx
    for m in range(1, n):
        print("A = " + str(A))
        # if start time >= finish time of last selection
        if a[m][0] >= a[k][1]:
            A.append(a[m])
            k = m
            print("adding a[%d]: " % (m) + str(a[m]))
    return A


def driver():
    #s = [1, 3, 0, 5, 3, 5,  6,  8,  8,  2, 12]
    #f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

    # a_i = (s_i, f_i)
    a = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), 
         (8, 12), (2, 14), (12, 16)]
    solution = greedy_activity_selector(a)
    print("SOLUTION: " + str(solution))


driver()