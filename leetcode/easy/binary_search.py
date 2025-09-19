from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        pivot = len(nums) // 2

        if target < nums[pivot]:
            return self.search(nums[:pivot], target)

        find = self.search(nums[pivot:], target)
        return pivot + find if find != -1 else -1


def test_task():
    s = Solution()
    assert s.search([0, 1, 5, 10], -3) == -1
    assert s.search([0, 1, 5, 10], 10) == 3
    assert s.search([0, 1, 5, 10], 0) == 0
    assert s.search([], 5) == -1
    assert s.search([1, 2, 3], 2) == 1


if __name__ == "__main__":
    test_task()
