"""
You are given a string s. We want to partition the string into as many parts as possible
 so that each letter appears in at most one part. For example, the string "ababcc" can
 be partitioned into ["abab", "cc"], but partitions such as
 ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order,
the resultant string should be s.

Return a list of integers representing the size of these parts.


Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into
less parts.


Example 2:

Input: s = "eccbbbbdec"
Output: [10]


Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""

from collections import Counter, defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)
        result = []

        for i in range(len(s)):
            last[s[i]] = i

        i = 0
        j = 0
        cur_length = 1
        while j < len(s):
            if last[s[i]] > j:
                cur_length += last[s[i]] - j
                j = last[s[i]]

            if i == j:
                result.append(cur_length)
                cur_length = 1
                j += 1

            i += 1

        return result

    def partitionLabels_counter(self, s: str) -> List[int]:
        c = Counter(s)
        cur = set()
        result = []
        cur_start = 0

        for i in range(len(s)):
            cur.add(s[i])
            c[s[i]] -= 1

            if c[s[i]] == 0:
                cur.remove(s[i])

            if not cur:
                result.append(i + 1 - cur_start)
                cur_start = i + 1

        return result


def test_task_counter():
    s = Solution()

    assert s.partitionLabels_counter("ababcc") == [4, 2]
    assert s.partitionLabels_counter("ababcbacadefegdehijhklij") == [9, 7, 8]


def test_task():
    s = Solution()

    assert s.partitionLabels("ababcc") == [4, 2]
    assert s.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]


if __name__ == "__main__":
    test_task()
    test_task_counter()
