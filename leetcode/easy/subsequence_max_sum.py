from typing import List


def max_straigh_subsequence(nums: List[int], k: int) -> List[int]:
    return max([nums[pos : pos + k] for pos in range(0, len(nums) - k + 1)], key=sum)


def test_max_straigh_subsequence():
    assert max_straigh_subsequence([2, 1, 3, 3], 2) == [3, 3]
    assert max_straigh_subsequence([-1, -2, 3, 4], 3) == [-2, 3, 4]
    assert max_straigh_subsequence([3, 4, 3, 3], 2) == [3, 4]


def max_subsequence(nums: List[int], k: int) -> List[int]:
    return [
        val[1]
        for val in sorted(
            sorted(enumerate(nums), key=lambda val: (val[1], -val[0]))[-k:],
            key=lambda val: val[0],
        )
    ]


def test_max_subsequence():
    assert max_subsequence([2, 1, 3, 3], 2) == [3, 3]
    assert max_subsequence([-1, -2, 3, 4], 3) == [-1, 3, 4]
    assert max_subsequence([3, 4, 3, 3], 2) == [3, 4]


if __name__ == "__main__":
    test_max_straigh_subsequence()
    test_max_subsequence()
