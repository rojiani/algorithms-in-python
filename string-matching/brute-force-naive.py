def naive_str_match(text, pattern):
    shifts = []
    m = len(pattern)
    n = len(text)
    for i in range(0, n - m + 1):
        if text[i:i+m] == pattern:
            shifts.append(i)
    return shifts

def naive_str_match_2(T, P):
    shifts = []
    m = len(P)
    n = len(T)
    s = 0
    while s <= n - m: 
        j = 0
        while j < m:
            if T[s+j] != P[j]:
                break
            j += 1
        if j == m:
            shifts.append(s)
        s += 1
    return shifts 

print(naive_str_match("abac", "abac"))
print(naive_str_match("abacabac", "abac"))
print(naive_str_match("abacabacabac", "abac"))
print(naive_str_match("abacxxxxxxxxabac", "abac"))
print('\n\n')
print(naive_str_match_2("abac", "abac"))
print(naive_str_match_2("abacabac", "abac"))
print(naive_str_match_2("abacabacabac", "abac"))
print(naive_str_match_2("abacxxxxxxxxabac", "abac"))
