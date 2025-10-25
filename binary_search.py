from typing import List

def feasible(mid: int, arr: List[int], target: int) -> bool:
    """
    Determines if the current mid value meets the condition.
    For a standard binary search, this checks whether arr[mid] >= target.
    You can modify this logic to fit your own feasibility condition.
    """
    return arr[mid] >= target

def binary_search(arr: List[int], target: int) -> int:
    """
    Binary search to find the first index where arr[mid] satisfies 'feasible'.
    Returns -1 if not found.
    """
    left, right = 0, len(arr) - 1
    first_true_index = -1

    while left <= right:
        mid = (left + right) // 2
        if feasible(mid, arr, target):
            first_true_index = mid
            right = mid - 1  # continue searching to the left
        else:
            left = mid + 1

    return first_true_index


if __name__ == "__main__":
    # Example usage
    arr = [1, 3, 5, 7, 9, 11, 13]
    target = 7

    index = binary_search(arr, target)

    if index != -1:
        print(f"First index where value >= {target} is {index} (value: {arr[index]})")
    else:
        print(f"No element in array is >= {target}")