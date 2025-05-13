"""
Timsort Algorithm in Python
This script implements the Timsort algorithm, which is a hybrid sorting algorithm derived from Merge Sort and Insertion Sort.
Timsort is designed to perform well on many kinds of real-world data. It divides the input into small chunks (called "runs"), sorts each run using Insertion Sort, and then merges the sorted runs using Merge Sort.
Timsort is the default sorting algorithm in Python (used by the built-in `sorted()` function and `list.sort()` method).
Time Complexity: O(n log n) in the worst, average, and best cases.
Space Complexity: O(n) due to the additional space used for merging runs.
"""

def timsort(arr):
    min_run = 32
    
    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    
    def merge(arr, left, mid, right):
        left_subarray = arr[left:mid + 1]
        right_subarray = arr[mid + 1:right + 1]
        i = j = 0
        k = left
        
        while i < len(left_subarray) and j < len(right_subarray):
            if left_subarray[i] <= right_subarray[j]:
                arr[k] = left_subarray[i]
                i += 1
            else:
                arr[k] = right_subarray[j]
                j += 1
            k += 1
        
        while i < len(left_subarray):
            arr[k] = left_subarray[i]
            i += 1
            k += 1
        
        while j < len(right_subarray):
            arr[k] = right_subarray[j]
            j += 1
            k += 1

    def timsort_helper(arr):
        n = len(arr)
        for i in range(0, n, min_run):
            insertion_sort(arr, i, min(i + min_run - 1, n - 1))
        
        size = min_run
        while size < n:
            for start in range(0, n, 2 * size):
                mid = min(n - 1, start + size - 1)
                end = min((start + 2 * size - 1), (n - 1))
                if mid < end:
                    merge(arr, start, mid, end)
            size *= 2
    
    timsort_helper(arr)
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", timsort(arr))
