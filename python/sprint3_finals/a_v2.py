"""
ID: .
Альтернативное решение к задаче "a" с использованием цикла.
"""


def broken_search(nums, target) -> int:
    left_idx = 0
    right_idx = len(nums) - 1

    while left_idx <= right_idx:

        mid_idx = (left_idx + right_idx) // 2

        if nums[mid_idx] == target:
            return mid_idx

        if (nums[left_idx] <= nums[mid_idx]
                and nums[left_idx] <= target < nums[mid_idx]):
            right_idx = mid_idx - 1
            continue

        if (nums[mid_idx] <= nums[right_idx]
            and not nums[mid_idx] < target <= nums[right_idx]):
            right_idx = mid_idx - 1
            continue

        left_idx = mid_idx + 1

    return -1
