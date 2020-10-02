# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    indexA = 0
    indexB = 0
    for index in range(0, len(merged_arr)):
        if arrA is not None:
            if arrA[indexA] <= arrB[indexB]:
                merged_arr[index] = arrA[indexA]
                if indexA < (len(arrA) - 1):
                    indexA += 1
                    print(indexA)
                else:
                    arrA = None
            else:
                merged_arr[index] = arrB[indexB]
                indexB += 1
                print(indexB)
        elif arrB is not None:
            merged_arr[index] = arrB[indexB]
            if indexB < (len(arrB) - 1):
                indexB += 1
                print(f'indexB after A is done: {indexB}')
            else:
                arrB = None



    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # split array in half until the length equals one
    if len(arr) == 1:
        return arr
    elif len(arr) > 1:
        return merge_sort(arr[0:((len(arr) - 1) // 2)])
        return merge_sort(arr[((len(arr) - 1) + 1):])


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
print(merge(arr1, arr2))