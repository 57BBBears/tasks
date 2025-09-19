from typing import List


def get_sum_indeces(nums: List[int], target: int) -> List[int]:
    complements = [target - num for num in nums]

    return [
        i
        for i in range(len(nums))
        if complements[i] in nums
        and not (complements[i] == nums[i] and nums.count(complements[i]) == 1)
    ]


def test_task():
    assert get_sum_indeces([3, 3], 6) == [0, 1]
    assert get_sum_indeces([2, 7, 11, 15], 9) == [0, 1]
    assert get_sum_indeces([3, 2, 4], 6) == [1, 2]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mb_nums = {}

        for i in range(len(nums)):
            if nums[i] in mb_nums:
                return [mb_nums[nums[i]], i]

            mb_nums[target - nums[i]] = i


def test_solution():
    s = Solution()

    assert s.twoSum([3, 3], 6) == [0, 1]
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]


if __name__ == "__main__":
    test_task()
    test_solution()
