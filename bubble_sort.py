"""
Insertion Sort Algorithm in Python
This script implements the Insertion Sort algorithm to sort a list of numbers in ascending order.
The Insertion Sort algorithm builds the final sorted array one item at a time by comparing each new element with the ones already sorted and inserting it into the correct position.
It is much like sorting a hand of cards, where you take one card at a time and place it in the correct spot among the already sorted ones.
Time Complexity: O(n^2) in the worst and average case, O(n) in the best case (when the array is already sorted).
Space Complexity: O(1) as it only requires a constant amount of additional space.
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", insertion_sort(arr))
