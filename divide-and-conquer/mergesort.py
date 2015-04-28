
# assume length(A) > 0
def mergesort(A):
    n = len(A)
    if n == 1:
        return A
    else:
        mid = int(n/2)
        left =  mergesort(A[0:mid]) 
        right = mergesort(A[mid:n])
        return merge(left, right)

def merge(left, right):
    n_left = len(left)
    n_right = len(right)
    aux = [None] * (n_left + n_right)
    idx_l = idx_r = idx_aux = 0

    while idx_l < n_left and idx_r < n_right:
        if left[idx_l] > right[idx_r]:
            aux[idx_aux] = right[idx_r]
            idx_r += 1
            idx_aux += 1
        else:
            aux[idx_aux] = left[idx_l]
            idx_l += 1
            idx_aux += 1

    while idx_r < n_right:
        aux[idx_aux] = right[idx_r]
        idx_r += 1
        idx_aux += 1
    while idx_l < n_left:
        aux[idx_aux] = left[idx_l]
        idx_l += 1        
        idx_aux += 1
        
    return aux



