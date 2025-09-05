def convert(s: str, numRows: int) -> str:
    """Convert a string into zigzag represantation according to row nums
    and return row by row. E.g. abcdefg, 3 -> aebdfcg
    a   e
    b d f
    c   g
    """
    revert_part_len = max(numRows - 2, 0)
    gap = numRows + revert_part_len
    result = ""

    for row in range(numRows):
        i = row

        if row == 0 or row == numRows - 1:
            while i < len(s):
                result += s[i]
                i += gap
        else:
            while i < len(s):
                # change the gap depending on odd or even column
                result += s[i]
                i += gap - row * 2 if (i - row) % gap == 0 else row * 2

    return result


def test_task():
    assert convert("A", 1) == "A"
    assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"


if __name__ == "__main__":
    test_task()
