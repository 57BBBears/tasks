"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.


Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true


Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        mid = 0

        while low < high:
            mid = (low + high) // 2

            if target < matrix[mid][0]:
                high = mid - 1
            elif target >= matrix[mid + 1][0]:
                low = mid + 1
            else:
                low = high = mid

        if low == high:
            row = matrix[low]
            low = 0
            high = len(row) - 1

            while low <= high:
                mid = (low + high) // 2

                if target == row[mid]:
                    return True
                elif target < row[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

        return False


def test_task():
    s = Solution()
    assert s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
    assert s.searchMatrix([[1]], 1)
    assert not s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)


if __name__ == "__main__":
    test_task()
