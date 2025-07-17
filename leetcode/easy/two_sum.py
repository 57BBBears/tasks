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


if __name__ == "__main__":
    test_task()
