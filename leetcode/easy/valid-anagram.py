from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (s_len := len(s)) != len(t):
            return False

        s_dict, t_dict = defaultdict(int), defaultdict(int)

        for i in range(s_len):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1

        return s_dict == t_dict


def test_task():
    s = Solution()

    assert s.isAnagram("", "")
    assert s.isAnagram("eat", "tea")
    assert not s.isAnagram("not", "anagram")


if __name__ == "__main__":
    test_task()
