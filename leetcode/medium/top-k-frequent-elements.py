"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]


Example 2:

Input: nums = [1], k = 1

Output: [1]


Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.
"""

import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        heap = [(-freq, num) for num, freq in c.most_common(k)]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        return [num for num, _ in c.most_common(k)]


def test_task():
    s = Solution()

    assert s.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert s.topKFrequent([1], 1) == [1]
    assert s.topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2) == [1, 2]


def test_task_heap():
    s = Solution()

    assert s.topKFrequent_heap([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert s.topKFrequent_heap([1], 1) == [1]
    assert s.topKFrequent_heap([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2) == [1, 2]


if __name__ == "__main__":
    test_task()
    test_task_heap()
