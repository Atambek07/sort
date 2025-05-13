"""
Merge Sort Algorithm in Python
This script implements the Merge Sort algorithm to sort a list of numbers in ascending order.
Merge Sort is a divide-and-conquer algorithm. It divides the array into two halves, sorts each half recursively, and then merges the sorted halves back together.
The merging step ensures that the array is sorted by combining two smaller sorted arrays into a larger sorted array.
Time Complexity: O(n log n) in all cases (best, average, and worst).
Space Complexity: O(n) due to the additional space required for merging.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", merge_sort(arr))
