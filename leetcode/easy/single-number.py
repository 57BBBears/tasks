"""
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant
extra space.


Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1


Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

Решить за O(1).
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber_xor(self, nums: List[int]) -> int:
        prev = 0
        for num in nums:
            prev = prev ^ num

        return prev


def test_task():
    s = Solution()
    assert s.singleNumber([2, 2, 1]) == 1
    assert s.singleNumber([4, 1, 2, 1, 2]) == 4
    assert s.singleNumber([1]) == 1


def test_task_xor():
    s = Solution()
    assert s.singleNumber_xor([2, 2, 1]) == 1
    assert s.singleNumber_xor([4, 1, 2, 1, 2]) == 4
    assert s.singleNumber_xor([1]) == 1


if __name__ == "__main__":
    test_task()
