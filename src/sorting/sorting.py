# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # keep track of indexes for three separate arrays
    indexA = 0
    indexB = 0
    index_merged = 0

    # the arrays being compared could be different lengths and
    # one will reach the end before the other; while neither is
    # at the end, compare the two values, insert the lower value
    # into the merged_arr, and increment the indexes for those two.
    while indexA < len(arrA) and indexB < len(arrB):
        if arrA[indexA] <= arrB[indexB]:
            merged_arr[index_merged] = arrA[indexA]
            index_merged += 1
            indexA += 1
        else:
            merged_arr[index_merged] = arrB[indexB]
            index_merged += 1
            indexB += 1
    
    # if arrB finished first, go throught the rest of arrA
    # and insert its values into merged_arr
    while indexA < len(arrA):
        merged_arr[index_merged] = arrA[indexA]
        index_merged += 1
        indexA += 1

    # if arrA finished first, go throught the rest of arrB
    # and insert its values into merged_arr
    while indexB < len(arrB):
        merged_arr[index_merged] = arrB[indexB]
        index_merged += 1
        indexB += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # split array in half until the length equals one
    # print(arr)
    if len(arr) > 1:
        left_array = arr[:((len(arr)) // 2)]
        right_array = arr[((len(arr)) // 2):]
        left_array = merge_sort(left_array)
        right_array = merge_sort(right_array)
        arr = merge(left_array, right_array)
        # print(f'in merge_sort before return: {arr}')

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

arr1 = [1, 5, 8, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr1))

arr2 = [4, 10, 13, 12]
# print(merge(arr1, arr2))