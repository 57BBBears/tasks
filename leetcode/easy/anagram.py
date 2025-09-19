def check_anagrams(word1: str, word2: str) -> bool:
    if (word_len := len(word1)) != len(word2):
        return False

    dict1 = {}
    dict2 = {}

    for i in range(word_len):
        dict1[word1[i]] = dict1.get(word1[i], 0) + 1
        dict2[word2[i]] = dict2.get(word2[i], 0) + 1

    return dict1 == dict2


def str_counter(string: str) -> dict:
    """
    Return counts of letters in a string as a dict.
    """
    result = {}

    for s in string:
        result[s] = result.get(s, 0) + 1

    return result


def check_anagrams_counter(word1: str, word2: str) -> bool:
    return str_counter(word1) == str_counter(word2)


def test_task():
    assert check_anagrams("lipa", "pila")
    assert not check_anagrams("not", "anagram")
    assert not check_anagrams("not", "yet")
    assert not check_anagrams("not", "notoh")
    assert check_anagrams("", "")
    assert check_anagrams("test", "test")


def test_task_counter():
    assert check_anagrams_counter("lipa", "pila")
    assert not check_anagrams_counter("not", "anagram")
    assert not check_anagrams_counter("not", "yet")
    assert not check_anagrams_counter("not", "notoh")
    assert check_anagrams_counter("", "")
    assert check_anagrams_counter("test", "test")


if __name__ == "__main__":
    test_task()
