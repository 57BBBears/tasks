"""
Вы профессиональный грабитель, планирующий ограбить дома на улице.
В каждом доме хранится определённое количество денег.
Единственное ограничение, которое мешает ограбить каждый из них, заключается в том,
что соседние дома оснащены системой безопасности, которая автоматически вызовет полицию,
если два соседних дома будут ограблены в одну ночь.

Дан целочисленный массив nums, представляющий количество денег в каждом доме.
Верните максимальное количество денег, которое вы можете ограбить этой ночью,
не привлекая внимания полиции.

Пример 1:

Ввод: nums = [1,2,3,1]

Вывод: 4

Объяснение: Ограбьте дом 1 (деньги = 1), а затем дом 3 (деньги = 3).

Общая сумма, которую вы можете ограбить = 1 + 3 = 4.

Пример 2:

Ввод: nums = [2,7,9,3,1]

Вывод: 12

Объяснение: Ограбьте дом 1 (деньги = 2), дом 3 (деньги = 9) и дом 5 (деньги = 1).

Общая сумма, которую вы можете ограбить = 2 + 9 + 1 = 12.

Ограничения:

1 <= nums.length <= 100

0 <= nums[i] <= 400
"""


def rob(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    else:
        return max(graph_max(nums, 0), graph_max(nums, 1))


def graph_max(graph: list[int], start: int) -> int:
    sums = {i: 0 for i in range(len(graph))}
    sums[start] = graph[start]
    stack = [start]

    forbidden = set()

    while stack:
        cur_i = stack[-1]

        if cur_i in forbidden:
            # backtrack
            stack.pop()
            forbidden.remove(cur_i)
            # discard neighbors if it's not common ones with prev or next
            if (cur_i - 2) not in forbidden:
                forbidden.discard(cur_i - 1)

            if (cur_i + 2) not in forbidden:
                forbidden.discard(cur_i + 1)

            continue

        forbidden |= {cur_i - 1, cur_i, cur_i + 1}

        for move in sums:
            if move not in forbidden:
                new_sum = sums[cur_i] + graph[move]
                if new_sum > sums[move]:
                    sums[move] = new_sum
                    stack.append(move)

    return max(sums.values())


def rob_optimized(nums: list[int]) -> int:
    if not list:
        return 0

    prev_max = 0
    cur_max = 0

    for num in nums:
        temp = cur_max

        cur_max = max(prev_max + num, cur_max)

        prev_max = temp

    return cur_max


def test_rob():
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([5, 1, 1, 5]) == 10
    assert rob([2, 4, 8, 9, 9, 3]) == 19


def test_rob_optimized():
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([5, 1, 1, 5]) == 10
    assert rob([2, 4, 8, 9, 9, 3]) == 19


if __name__ == "__main__":
    test_rob()
    test_rob_optimized()
