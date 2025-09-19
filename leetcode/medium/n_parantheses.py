def generate(current: str, open: int, closed: int, n: int):
    if len(current) == 2 * n:
        print(current)
        return

    if open < n:
        generate(current + "(", open + 1, closed, n)

    if closed < open:
        generate(current + ")", open, closed + 1, n)


def parenthes(n):
    generate("", 0, 0, n)


if __name__ == "__main__":
    parenthes(3)
