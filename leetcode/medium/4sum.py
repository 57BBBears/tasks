"""
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.


Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 3):
            # skip duplicated starting values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                # skip duplicated starting values
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = len(nums) - 1

                while left < right:
                    cur_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if cur_sum == target:
                        cur = [nums[i], nums[j], nums[left], nums[right]]
                        result.append(cur)
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif cur_sum < target:
                        left += 1
                    else:
                        right -= 1

        return result


def test_task():
    s = Solution()

    assert s.fourSum([], 0) == []
    assert s.fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
    assert s.fourSum([1, 0, -1, 0, -2, 2], 0) == [
        [-2, -1, 1, 2],
        [-2, 0, 0, 2],
        [-1, 0, 0, 1],
    ]
    assert s.fourSum([-3, -1, 0, 2, 4, 5], 0) == [[-3, -1, 0, 4]]
    assert s.fourSum([-3, -1, 0, 2, 4, 5], 2) == [[-3, -1, 2, 4]]


if __name__ == "__main__":
    test_task()
