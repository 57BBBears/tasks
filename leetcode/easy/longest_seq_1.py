from typing import List


def get_longest_seq(nums: List[int]) -> int:
    max_len = 0
    cur_max = 0

    for num in nums:
        if num == 1:
            cur_max += 1
        elif cur_max:
            max_len = max(cur_max, max_len)
            cur_max = 0

    return max(cur_max, max_len)


def test_task():
    assert get_longest_seq([1, 1, 1, 0, 0, 1, 1]) == 3
    assert get_longest_seq([1, 0, 1, 0, 1]) == 1
    assert get_longest_seq([1, 1, 1, 1, 1]) == 5
    assert get_longest_seq([0]) == 0
    assert get_longest_seq([]) == 0


if __name__ == "__main__":
    test_task()
