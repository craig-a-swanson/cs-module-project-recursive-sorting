
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

def merge_sort(arr):
    # split array in half until the length equals one
    # print(arr)
    if len(arr) > 1:
        left_array = arr[:((len(arr)) // 2)]
        right_array = arr[((len(arr)) // 2):]
        # print(f'left before left call: {left_array}')
        left_array = merge_sort(left_array)
        # print(f'left after left call: {left_array}')
        # print(f'right before right call: {right_array}')
        right_array = merge_sort(right_array)
        # print(f'right after right call: {right_array}')
        arr = merge(left_array, right_array)
        # print(f'in merge_sort before return: {arr}')
    # print(f'array before return: {arr}')
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    # essentailly comparing two arrays:
    # the first array is the first half of this array (to the mid-point)
    # the second array is the second half of this array (mid-point + 1 to the end)
    right_pointer = mid + 1

    while start <= mid and right_pointer <= end:
        if arr[start] <= arr[right_pointer]:
            start += 1
        else:
            # make the value of arr[start] equal to arr[right_pointer]
            # and move the elements in between to the right by one
            temp_value = arr[right_pointer]
            index = right_pointer

            # loop to set current element equal to value of previous element
            # iterate backwards through array
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            
            # the start index element is changed to the value of the temp_value
            arr[start] = temp_value
            # all the pointers move up
            start += 1
            right_pointer += 1
            mid += 1

    return arr

# [3, 44, 38, 5]

def merge_sort_in_place(arr, l, r):
    if l < r:
        mid = (l + (r - 1)) // 2

        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)
        # print(f'arr: {arr} start {l} mid {mid} end {r}')
        arr = merge_in_place(arr, l, mid, r)
        # print(f'before return {arr}')
    return arr
