
# Longest Common Subsequence
# not finished - bug if strings of 2 diff lengths

def lcs(x, y):
    x_len = len(x)
    y_len = len(y)
    # Two 2D matrices, 1 for values, 1 for arrows
    c = [[0 for i in range(x_len)] for j in range(y_len)]
    arrows = [['X' for i in range(x_len)] for j in range(y_len)]
    print_2d_array(c)
    print_2d_array(arrows)
    for i in range(x_len):
        for j in range(y_len):
            # all values initially 0, so nothing special if i,j = 0
            print("i,j = %d,%d; x[i]=%s, y[j]=%s" % (i, j, x[i], y[j]))
            if i == 0 or j == 0:
                continue
            elif x[i] == y[j]: 
                # match
                print("ERROR i,j = %d,%d; x[i]=%s, y[j]=%s" % (i, j, x[i], y[j]))
                c[i][j] = c[i-1][j-1] + 1
                arrows[i][j] = "\\"                
            else:
                left = c[i-1][j]
                up = c[i][j-1]
                if left >= up:
                    c[i][j] = left
                    arrows[i][j] = '<'
                else:
                    c[i][j] = up
                    arrows[i][j] = '^'
    print_2d_array(c)
    print_2d_array(arrows)
    backtrack(arrows, x, y)
    return c

def backtrack(arrows, x, y):
    i = len(x) - 1
    j = len(y) - 1
    rev_lcs = ""
    while i > 0 and j > 0:
        if arrows[i][j] == '<':
            i -= 1
            continue
        if arrows[i][j] == '^':
            j -= 1
            continue
        if arrows[i][j] == '\\':
            if x[i] != y[j]:
                print("ERROR")
            rev_lcs += x[i]
            i -= 1
            j -= 1
            continue
    # reverse
    lcs = ''.join([rev_lcs[x] for x in range(len(rev_lcs)-1, -1, -1)])
    print("LCS: " + lcs)
    return lcs

# http://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python
def print_2d_array(matrix):
    for row in matrix:
        for val in row:
            print('{:4}'.format(val), end="")
        print("")

lcs("TCTGATGC", "GGCAGTCT")
lcs("xaaxaxa", "aaaa")
#lcs("aaaa", "xaaxaxa")

