# Counts the number of inversions in a list A

# Driver function
#   Prints list of inversions
#   Returns number of inversions
def inversions(A):
    if len(A) == 0:
        print("Empty list. No inversions.")
        return 0

    if has_duplicates(A):
        print("List cannot contain duplicates.")
        return 0

    inversion_list = []
    sort_and_count(A, inversion_list)
    print("Inversions: %s" % (str(inversion_list)))
    return len(inversion_list)

# assume length(A) > 0
def sort_and_count(A, inv):
    n = len(A)
    if n == 1:
        return A
    else:
        mid = int(n/2)
        left = sort_and_count(A[0:mid], inv)
        right = sort_and_count(A[mid:n], inv)
        aux = merge_and_count(left, right, inv)
        return aux


# Returns: (merged_array, inv_list)
def merge_and_count(left, right, inv):
    left_sz = len(left)
    right_sz = len(right)
    aux = [None] * (left_sz + right_sz)
    idx_l = idx_r = idx_aux = 0

    while idx_l < left_sz and idx_r < right_sz:
        if left[idx_l] > right[idx_r]:
            inversion_str = '(' + str(left[idx_l]) + ',' + str(right[idx_r]) + ')';
            inv.append(inversion_str)            
            aux[idx_aux] = right[idx_r]
            idx_r += 1
            idx_aux += 1        
        else:
            aux[idx_aux] = left[idx_l]
            idx_l += 1
            idx_aux += 1

    while idx_r < right_sz:
        aux[idx_aux] = right[idx_r]
        idx_r += 1
        idx_aux += 1
    while idx_l < left_sz:
        aux[idx_aux] = left[idx_l]
        idx_l += 1        
        idx_aux += 1
        
    return aux


def has_duplicates(lst):
    return len(lst) != len(set(lst))

