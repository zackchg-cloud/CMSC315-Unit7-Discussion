Unit 7 Discussion: Sorting Algorithms
Overview

This assignment compared Bubble Sort and Merge Sort using multiple datasets and edge-case testing. Both algorithms were implemented in Python and tested to verify that they correctly sorted various lists.

Learning Objectives Completed
Implemented Bubble Sort
Implemented Merge Sort
Applied divide-and-conquer concepts through recursion
Compared algorithm efficiency and performance characteristics
Tested multiple datasets and edge cases
Program Description
Bubble Sort

Bubble Sort was implemented by repeatedly comparing adjacent elements and swapping them when they were out of order. The algorithm continued making passes through the list until all values were sorted.

Merge Sort

Merge Sort was implemented using recursion. The list was repeatedly divided into smaller halves until each section contained one element. The sorted halves were then merged back together into a fully sorted list.

Datasets Tested
Dataset #1
Plain Text
[64, 34, 25, 12, 22, 11, 90]
Dataset #2
Plain Text
[45, 18, 72, 3, 57, 29, 81, 10]

Both Bubble Sort and Merge Sort produced identical sorted results for both datasets.

Edge Cases Tested
Empty List
Plain Text
[]
 

Result: Both algorithms returned an empty list without errors.

Already Sorted List
Plain Text
[1, 2, 3, 4, 5]

Result: Both algorithms correctly preserved the sorted order.

List with Duplicate Values
Plain Text
[4, 2, 4, 1, 2]

Result: Both algorithms correctly sorted the list while maintaining duplicate values.

Reverse Sorted List
Plain Text
[9, 8, 7, 6, 5]

Result: Both algorithms successfully sorted the list into ascending order.

Reflection

While completing this assignment, I learned how different sorting algorithms approach the same problem. Bubble Sort used repeated comparisons and swaps between adjacent elements, while Merge Sort used a divide-and-conquer strategy that recursively split the list into smaller sections before merging them back together. This helped me better understand recursion and algorithm design.

The most challenging part of the assignment was understanding how Merge Sort continuously divided the list and then reconstructed the sorted result during the merge process. I overcame this challenge by tracing the algorithm step-by-step and observing how the recursive calls worked together.

Bubble Sort and Merge Sort both produced the same results, but they differed significantly in efficiency. Bubble Sort has a time complexity of O(n²), making it less efficient for large datasets because every element may need to be compared multiple times. Merge Sort has a time complexity of O(n log n), allowing it to handle larger datasets much more efficiently. The tradeoff is that Merge Sort requires additional memory and is more complex to implement. Bubble Sort may be suitable for small datasets or educational purposes, while Merge Sort is generally a better choice for large-scale applications where performance is important.