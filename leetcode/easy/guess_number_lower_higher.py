# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
#     ...


picked_num = 6


def guess(num: int) -> int:
    if num < picked_num:
        return 1
    elif num > picked_num:
        return -1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int | None:
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            if guess(mid) == 1:
                left = mid + 1
            elif guess(mid) == -1:
                right = mid - 1
            else:
                return mid


def test_task():
    s = Solution()
    assert s.guessNumber(picked_num) == picked_num


if __name__ == "__main__":
    test_task()
