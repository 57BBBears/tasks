"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally
 or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1


Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        i, j = 0, 0
        row_len = len(grid[0])

        for i in range(len(grid)):
            for j in range(row_len):
                if grid[i][j] == "0":
                    continue

                checks = [(i, j)]

                while checks:
                    cur = checks.pop()
                    grid[cur[0]][cur[1]] = "0"

                    new_i = cur[0] + 1
                    new_j = cur[1] + 1
                    prev_i = cur[0] - 1
                    prev_j = cur[1] - 1

                    if new_i != len(grid) and grid[new_i][cur[1]] == "1":
                        checks.append((new_i, cur[1]))

                    if new_j != row_len and grid[cur[0]][new_j] == "1":
                        checks.append((cur[0], new_j))

                    if prev_i > -1 and grid[prev_i][cur[1]] == "1":
                        checks.append((prev_i, cur[1]))

                    if prev_j > -1 and grid[cur[0]][prev_j] == "1":
                        checks.append((cur[0], prev_j))

                count += 1

        return count


def test_task():
    s = Solution()

    assert (
        s.numIslands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )
    assert (
        s.numIslands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )
    assert s.numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]) == 1


if __name__ == "__main__":
    test_task()
