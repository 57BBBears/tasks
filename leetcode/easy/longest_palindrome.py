def longest_palindrome(s: str) -> int:
    letters = {}

    for letter in s:
        letters[letter] = letters.setdefault(letter, 0) + 1

    cur_cum = sum(map(lambda v: round(v // 2) * 2, letters.values()))

    return cur_cum + 1 if any([v % 2 != 0 for v in letters.values()]) else cur_cum


def test_task():
    assert longest_palindrome("ccc") == 3
    assert longest_palindrome("bb") == 2
    assert longest_palindrome("bbccccd") == 7


if __name__ == "__main__":
    test_task()
