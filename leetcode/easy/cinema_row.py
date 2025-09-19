"""
You are choosing a seat in a cinema row. You have take an unoccupaied seat as far as
possible from your neighbors. A row contains at least one occupaied and one free seats.

Function gets a list of 1 and 0. Free seat is 0, occupied is 1.

Return maximum distance from your seat to the nearest occupied seat.


Example 1:

Input: seats = [1, 0, 0, 0, 1]

Output: 2


Example 2:

Input: seats = [1, 1, 0, 0, 0]

Output: 3


Example 3:

Input: seats = [0, 0, 0, 0, 1]

Output: 4
"""


def get_distance(seats: list[int]) -> int:
    left, right = -1, 0
    distance = 0

    for right in range(len(seats)):
        if seats[right] == 1:
            if left == -1:
                distance = right
            else:
                distance = max(distance, (right - left) // 2)

            left = right

    return max(distance, right - left)


def test_task():
    assert get_distance([1, 0, 0, 0, 1]) == 2
    assert get_distance([1, 1, 0, 0, 0]) == 3
    assert get_distance([0, 0, 0, 0, 1]) == 4
    assert get_distance([1, 0, 1, 0, 1]) == 1


if __name__ == "__main__":
    test_task()
