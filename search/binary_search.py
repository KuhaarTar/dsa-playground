from typing import Any


def binary_search(nums: [], element: Any) -> bool:
    """
    Implement binary search
    :param nums: Expected already sorted array
    :param element: Element in array to found
    :return: boolean if element is founded or not
    """
    end = len(nums) - 1
    start = 0
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == element:
            return True
        if nums[mid] > element:
            end = mid - 1
        if nums[mid] < element:
            start = mid + 1
    return False


print(binary_search([1, 2, 7, 10, 14, 20, 75], 200))
