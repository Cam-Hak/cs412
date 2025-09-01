#
# Input: Array arr of values and search  key
# Output: The index of key in the array arr, if present, or -1 otherwise
# Coded by: Duan Bowers
# 

# Searches an array of a sorted array arr for an element key. 
# The array is the array(subarray) starting at index low and ending
# on index high(inclusive).
def binarySearch(arr, low, high, key):
    
    # If the array is empty, return -1
    if high < low:
        return -1
 
    # Get the mid point index of the array with low to high
    mid = (low + high)//2
 
    # if arr[mid] is the key, return mid point.
    if key == arr[mid]:
        return mid
    
    # If the key is larger than arr[mid], then we reduce the problem to finding the 
    # index in the second half(right half) of the array
    if key > arr[mid]:
        return binarySearch(arr, (mid + 1), high, key)
    # Reduce the problem to searching the left half of the array. 
    return binarySearch(arr, low, (mid - 1), key)

