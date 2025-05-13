# Sorting Algorithms in Python

This repository contains Python implementations of various sorting algorithms, demonstrating different approaches to sorting a list of numbers. The implemented algorithms include:

- Bubble Sort
- Insertion Sort
- Selection Sort
- Quick Sort
- Merge Sort
- Timsort (Python's built-in sorting algorithm)

## Algorithms

### 1. **Bubble Sort**
Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

- **Time Complexity**: O(n²) in the worst and average case, O(n) in the best case (when the array is already sorted).
- **Space Complexity**: O(1)

### 2. **Insertion Sort**
Insertion Sort builds the final sorted array one item at a time. It works by comparing each new element with the already sorted part and inserting it in the correct position.

- **Time Complexity**: O(n²) in the worst and average case, O(n) in the best case (when the array is already sorted).
- **Space Complexity**: O(1)

### 3. **Selection Sort**
Selection Sort divides the list into two parts: a sorted part and an unsorted part. It repeatedly selects the smallest element from the unsorted part and swaps it with the first unsorted element.

- **Time Complexity**: O(n²) in the worst, average, and best cases.
- **Space Complexity**: O(1)

### 4. **Quick Sort**
Quick Sort is a divide-and-conquer algorithm. It selects a pivot element and partitions the other elements into two sub-arrays (less than or greater than the pivot), recursively sorting them.

- **Time Complexity**: O(n log n) on average, O(n²) in the worst case (when the pivot is poorly chosen).
- **Space Complexity**: O(log n) in the average case, O(n) in the worst case (due to recursion stack).

### 5. **Merge Sort**
Merge Sort is another divide-and-conquer algorithm. It divides the array into two halves, recursively sorts them, and then merges the sorted halves.

- **Time Complexity**: O(n log n) in all cases (best, average, and worst).
- **Space Complexity**: O(n) due to the additional space required for merging.

### 6. **Timsort**
Timsort is a hybrid sorting algorithm derived from Merge Sort and Insertion Sort. It divides the input into small chunks (runs), sorts each run using Insertion Sort, and then merges the runs using Merge Sort.

- **Time Complexity**: O(n log n) in the worst, average, and best cases.
- **Space Complexity**: O(n) due to the additional space required for merging.

Timsort is the default sorting algorithm in Python, used by the built-in `sorted()` function and `list.sort()` method.

# Installation
- Clone this repository:

``` bash
git clone https://github.com/your-username/sorting-algorithms.git
cd sorting-algorithms
```
- Run the Python scripts for any sorting algorithm you want to test.

## Contributing
Feel free to fork this repository and submit pull requests for any improvements or additional sorting algorithms you would like to add.
