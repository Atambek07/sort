"""
Selection Sort Algorithm in Python
This script implements the Selection Sort algorithm to sort a list of numbers in ascending order.
The Selection Sort algorithm divides the list into two parts: a sorted part and an unsorted part. It repeatedly selects the smallest (or largest, depending on the sorting order) element from the unsorted part and swaps it with the first unsorted element, thus expanding the sorted part.
Time Complexity: O(n^2) in the worst, average, and best cases.
Space Complexity: O(1) as it only requires a constant amount of additional space.
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", selection_sort(arr))
