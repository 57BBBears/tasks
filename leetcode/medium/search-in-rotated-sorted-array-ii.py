"""
There is an integer array nums sorted in non-decreasing order (not necessarily with
distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k
(0 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become
[4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is
in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.


Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true


Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104


Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may
contain duplicates. Would this affect the runtime complexity? How and why?
"""

from typing import List


class Solution:
    def search_recur(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        left = 0
        right = len(nums) - 1

        mid = (left + right) // 2

        if nums[mid] == target:
            return True

        return self.search_recur(nums[:mid], target) or self.search_recur(
            nums[mid + 1 :], target
        )

    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        left = 0
        right = len(nums) - 1

        mid = (left + right) // 2

        if nums[mid] == target:
            return True

        if nums[mid] < nums[right] and nums[mid] < target <= nums[right]:
            return self.search(nums[mid + 1 :], target)

        if nums[mid] > nums[left] and nums[left] <= target < nums[mid]:
            return self.search(nums[:mid], target)

        return self.search(nums[mid + 1 :], target) or self.search(nums[:mid], target)


def test_task_recur():
    s = Solution()
    assert not s.search_recur([2, 5, 6, 0, 0, 1, 2], 3)
    assert s.search_recur([2, 5, 6, 0, 0, 1, 2], 0)
    assert s.search_recur([1, 1, 1, 0, 0], 0)
    assert not s.search_recur([1, 1, 1, 0, 0], 3)
    assert s.search_recur([1, 0, 1, 1, 1], 0)


def test_task():
    s = Solution()
    assert not s.search([2, 5, 6, 0, 0, 1, 2], 3)
    assert s.search([2, 5, 6, 0, 0, 1, 2], 0)
    assert s.search([1, 1, 1, 0, 0], 0)
    assert not s.search([1, 1, 1, 0, 0], 3)
    assert s.search([1, 0, 1, 1, 1], 0)
    assert s.search([3, 5, 1], 1)


if __name__ == "__main__":
    test_task()
    test_task_recur()
