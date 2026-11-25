"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================
"""


def bubble_sort(lst):
    """Sort a list using Bubble Sort."""

    sorted_list = lst.copy()
    n = len(sorted_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j]
                )

    return sorted_list


def merge_sort(lst):
    """Sort a list using Merge Sort."""

    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    """Merge two sorted lists into one sorted list."""

    merged = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    print("\n=== DATASET #1 ===")

    dataset1 = [64, 34, 25, 12, 22, 11, 90]

    print("Original:", dataset1)
    print("Bubble Sort:", bubble_sort(dataset1))
    print("Merge Sort :", merge_sort(dataset1))

    print("\n=== DATASET #2 ===")

    dataset2 = [45, 18, 72, 3, 57, 29, 81, 10]

    print("Original:", dataset2)
    print("Bubble Sort:", bubble_sort(dataset2))
    print("Merge Sort :", merge_sort(dataset2))

    print("\n=== EDGE CASE TESTS ===")

    empty_list = []
    print("\nEmpty List:")
    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort :", merge_sort(empty_list))

    sorted_list = [1, 2, 3, 4, 5]
    print("\nAlready Sorted List:")
    print("Bubble Sort:", bubble_sort(sorted_list))
    print("Merge Sort :", merge_sort(sorted_list))

    duplicate_list = [4, 2, 4, 1, 2]
    print("\nList With Duplicates:")
    print("Bubble Sort:", bubble_sort(duplicate_list))
    print("Merge Sort :", merge_sort(duplicate_list))

    reverse_list = [9, 8, 7, 6, 5]
    print("\nReverse Sorted List:")
    print("Bubble Sort:", bubble_sort(reverse_list))
    print("Merge Sort :", merge_sort(reverse_list))


if __name__ == "__main__":
    main()