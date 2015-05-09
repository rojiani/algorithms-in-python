"""
Longest Common Subsequence
Dynamic Programming
CLRS 15.4
"""
from enum import Enum

class Arrow(Enum):
    up = '|'
    left = '<='
    diag = '\\'


def LCS(X, Y):
    # extend X and Y, so that indexing matches that in book
    orig_X, orig_Y = X,Y
    X = ' ' + X
    Y = ' ' + Y

    n,m = len(X),len(Y)
    rows,cols = n,m

    c = [[None for j in range(cols)] for i in range(rows)]
    arrows = [[None for c in range(cols)] for r in range(rows)]

    for i in range(rows):
        c[i][0] = 0
    for j in range(cols):
        c[0][j] = 0

    for i in range(1, n):
        for j in range(1, cols):
            # print("[%d][%d]" % (i,j))
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
                arrows[i][j] = Arrow.diag
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
                arrows[i][j] = Arrow.left if c[i-1][j] >= c[i][j-1] else Arrow.up

    Z = solve_LCS(c, arrows, X, Y)
    print("The LCS of %s and %s is %s (length = %d)" % (X,Y,Z, len(Z)))
    return len(Z)


def solve_LCS(c, arrows, X, Y):
    Z_rev = ''
    n,m = len(X),len(Y)
    rows,cols = n,m

    i,j = rows-1,cols-1
    while i > 0 and j > 0:
        if arrows[i][j] == Arrow.diag:
            Z_rev += X[i]
            i,j = i-1, j-1
        elif arrows[i][j] == Arrow.up:
            j -= 1
        else:
            i -= 1
    return ''.join([Z_rev[i] for i in range(len(Z_rev)-1, -1, -1)])

def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print('{:4}'.format(val), end="")
        print()


LCS("ABCBDAB", "BDCABA")
LCS("GTTCCTAATA", "CGATAATTGAGA")
LCS("XMJYAUZ", "MZJAWXU")