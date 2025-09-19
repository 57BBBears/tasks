"""
You are given a string s and an integer k. You can choose any character of the string
and change it to any other uppercase English character. You can perform this operation
at most k times.

Return the length of the longest substring containing the same letter you can get after
performing the above operations.


Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.


Example 2:

Input: s = "AABABBA", k = 1


Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = {}
        char_max = 0
        left = 0
        result = 0

        for right in range(len(s)):
            right_char = s[right]
            char_counts[right_char] = char_counts.get(right_char, 0) + 1

            char_max = max(char_counts[right_char], char_max)

            while (right - left + 1) - char_max > k:
                left_char = s[left]

                char_counts[left_char] -= 1

                left += 1

            result = max(result, right - left + 1)

        return result


def test_task():
    s = Solution()
    print(s.characterReplacement("ABCDDD", 3))
    assert s.characterReplacement("ABAB", 2) == 4
    assert s.characterReplacement("ABBB", 2) == 4
    assert s.characterReplacement("BAAA", 0) == 3
    assert s.characterReplacement("ABCDDD", 3) == 6
    assert s.characterReplacement("AABABBA", 1) == 4
    assert s.characterReplacement("AABABBA", 0) == 2
    assert s.characterReplacement("AAABABBA", 0) == 3


if __name__ == "__main__":
    test_task()
