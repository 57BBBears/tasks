# Create the biggest number from the list of digits

from functools import reduce


def largest_number(nums: list[int]) -> str:
    max_digit_len = len(str(max(nums)))

    return "".join(
        map(
            str,
            sorted(nums, key=lambda num: -num * 10 ** (max_digit_len - len(str(num)))),
        )
    )


def largest_number_quick_sort(nums: list[int]) -> str:
    if len(nums) <= 1:
        return "".join(map(str, nums))

    pivot = nums[len(nums) // 2]
    left, middle, right = [], [], []

    for num in nums:
        if num == pivot:
            middle.append(str(num))
        elif int(str(num) + str(pivot)) > int(str(pivot) + str(num)):
            left.append(num)
        else:
            right.append(num)

    return largest_number(left).lstrip() + "".join(middle) + largest_number(right)


def largest_number_insert_sort(nums: list[int]) -> str:
    nums.sort(key=lambda num: -max(map(int, str(num))))

    for i in range(1, len(nums)):
        j = i - 1

        while j != -1:
            if (
                nums[i] * 10 ** len(str(nums[j])) + nums[j]
                > nums[j] * 10 ** len(str(nums[i])) + nums[i]
            ):
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                break

    return reduce(
        lambda num1, num2: "0"
        if str(num1) == "0" and str(num2) == "0"
        else str(num1) + str(num2),
        nums,
    )


def test_task():
    assert largest_number_insert_sort([10, 2]) == "210"
    assert largest_number_insert_sort([3, 30, 34, 5, 9]) == "9534330"
    assert largest_number_insert_sort([432, 43243]) == "43243432"
    assert largest_number_insert_sort([111311, 1113]) == "1113111311"
    assert largest_number_insert_sort([0, 0]) == "0"


if __name__ == "__main__":
    test_task()
