"""
Quick Sort Algorithm in Python
This script implements the Quick Sort algorithm to sort a list of numbers in ascending order.
Quick Sort is a divide-and-conquer algorithm. It selects a 'pivot' element from the array and partitions the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
The sub-arrays are then sorted recursively.
Time Complexity: O(n log n) on average, O(n^2) in the worst case (when the pivot elements are poorly chosen).
Space Complexity: O(log n) in the average case, O(n) in the worst case (due to recursion stack).
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", quick_sort(arr))
