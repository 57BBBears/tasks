import sys


def delete_nils(list_: list[int]):
    """
    Without list comprehension
    :param list_: a list of numbers
    :return: a list without nils
    """
    pivot = 0
    i = 0
    while i < len(list_):
        if list_[i] != 0:
            list_[pivot] = list_[i]
            pivot += 1

        i += 1

    return list_[:pivot]


if __name__ == "__main__":
    numbers = [int(sys.argv[i]) for i in range(1, len(sys.argv))]
    print(delete_nils(numbers))
