from random import randint, shuffle


def go_shuffle(players: list[str]) -> list[list[str]]:
    shuffle(players)

    for i in range(0, len(players) - 1):
        players[i] = [players[i], players[i + 1]]

    if players:
        players[-1] = [players[-1], players[0][0] if len(players) > 1 else ""]

    return players


def go(players: list[str]) -> list[list[str]]:
    if len(players) == 1:
        return [[players[0]]]

    gifts = players[:]
    i, j = 0, len(players) - 1

    while i <= j:
        gift = gifts.pop(randint(0, len(gifts) - 1))
        if gift == players[i]:
            if gifts:
                # not the last gift
                players[j] = [players[j], gift]
            else:
                # the last and same player and gift - replace gifts with the prev one
                replace_i = j - 1 if j != 0 else j + 1
                players[j] = [players[j], players[replace_i][1]]
                players[replace_i][1] = gift
            j -= 1
        else:
            players[i] = [players[i], gift]
            i += 1

    return players


if __name__ == "__main__":
    print(go_shuffle(["Willy", "Bob", "Chris", "Elly"]))
    print(go_shuffle(["Willy", "Bob", "Chris"]))
    print(go_shuffle(["Willy", "Bob"]))
    print(go_shuffle(["Willy"]))

    print(go(["Willy", "Bob", "Chris", "Elly"]))
    print(go(["Willy", "Bob", "Chris"]))
    print(go(["Willy", "Bob"]))
    print(go(["Willy"]))
