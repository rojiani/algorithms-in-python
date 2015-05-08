"""
C(n, k) using recurrence relation in Pascal's Triangle

C(n, k) = C(n-1, k-1) + C(n-1, k)

C(n, k) = choose[n][k]


Top-Down algorithm runs much faster?
"""


""" 
Bottom-Up
"""
DEFAULT_SZ = 60
table = [[0 for c in range(DEFAULT_SZ)] for r in range(DEFAULT_SZ)]
def n_choose_k(n, k):
   #print("nck(%d,%d)" % (n,k))
    if k == 0 or k == n: return 1
    # Fill all known values
    for i in range(n+1):
        table[n][0] = 1
        table[i][i] = 1

    for i in range(1, n+1):
        for j in range(1, i):
            # print("table[%d][%d] = table[%d][%d] + table[%d][%d]" % (n,k, (n-1),(k-1), (n-1),k))
            table[i][j] = table[i-1][j-1] + table[i-1][j]

    return table[n][k]

for n in range(11):
    for k in range(11):
        print("C(%d,%d) = %d" % (n,k, n_choose_k(n,k)))
    print()

# print(n_choose_k(8, 2))

# """ Using 2D List, Top-down """
table_2 = [[0 for c in range(DEFAULT_SZ)] for r in range(DEFAULT_SZ)]
def nck(n,k):
    for i in range(n+1):
        table_2[i][0] = 1
        table_2[i][i] = 1
    return nck_top_down(n,k)

def nck_top_down(n, k):
    if k > n: return 0
    if table_2[n][k] != 0:
        return table_2[n][k]
    else:
        table_2[n][k] = nck_top_down(n-1, k-1) + nck_top_down(n-1, k)
        return table_2[n][k]

for n in range(11):
    for k in range(11):
        print("C(%d,%d) = %d" % (n,k, nck(n,k)))
    print()


# print(nck(0,2))
#print(nck(50, 22))


