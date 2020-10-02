# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # if empty array, return -1
    # otherwise, find the midpoint and test its equal to target
    # if equal, return its index
    # if greater than target, set new "end" to midpoint index minus one and recurse
    # if less than target, set new "start" to midepoint index plus one and recurse
    # if start equals end, return -1

    if len(arr) == 0:
        return -1
    
    mid_point = (start + end) //  2
    print(arr[mid_point])
    if arr[mid_point] == target:
        return mid_point
    elif arr[mid_point] > target:
        end = mid_point
        return binary_search(arr, target, start, end)
    elif arr[mid_point] < target:
        start = mid_point
        return binary_search(arr, target, start, end)

    return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
