""" 
Given a sorted array arr[] and a number x, write a function that counts the 
occurrences of x in arr[]. Expected time complexity is O(log(n))
http://www.geeksforgeeks.org/count-number-of-occurrences-in-a-sorted-array/
"""

def count_x(arr, x):
    n = len(arr)
    if n == 0:
        return 0
    first,last = arr[0],arr[n-1]
    if last < x or first > x:
        return 0
    elif first == last and first == x:
        return n
    else:
        mid = int(n/2)
        return count_x(arr[:mid], x) + count_x(arr[mid:], x)



