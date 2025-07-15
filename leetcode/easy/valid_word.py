import re


def is_word_valid(word: str) -> bool:
    return bool(
        re.search(r"^[a-z0-9]{3,20}$", word, re.IGNORECASE)
        and re.search(
            r"[aeuio]+.?[bcdfghjklmnpqrstvwxyz]+|[bcdfghjklmnpqrstvwxyz]+.?[aeuio]+",
            word,
            re.IGNORECASE,
        )
    )


def test_is_word_valid():
    assert is_word_valid("234Adas")
    assert is_word_valid("AANN")
    assert not is_word_valid("b3")
    assert not is_word_valid("a3$e")


if __name__ == "__main__":
    test_is_word_valid()
