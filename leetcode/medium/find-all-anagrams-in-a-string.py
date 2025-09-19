"""
Given two strings s and p, return an array of all the start indices of p's anagrams
in s. You may return the answer in any order.


Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".


Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagram_dict = {}

        for letter in p:
            anagram_dict[letter] = anagram_dict.get(letter, 0) + 1

        indices = []

        cur = s[: len(p) - 1]
        cur_dict = {}

        for letter in cur:
            cur_dict.setdefault(letter, 0)
            cur_dict[letter] += 1

        for j in range(len(p) - 1, len(s)):
            i = j + 1 - len(p)

            cur_dict[s[j]] = cur_dict.get(s[j], 0) + 1

            if cur_dict == anagram_dict:
                indices.append(i)

            cur_dict[s[i]] -= 1

            if cur_dict[s[i]] == 0:
                del cur_dict[s[i]]

        return indices


def test_task():
    s = Solution()

    assert s.findAnagrams("abab", "ab") == [0, 1, 2]
    assert s.findAnagrams("cbaebabacd", "abc") == [0, 6]


if __name__ == "__main__":
    test_task()
