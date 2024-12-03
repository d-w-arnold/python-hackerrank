def sword_problem(i: int):
    """
    There are one hundred people standing in a circle.
    They count off beginning at one and ending at one hundred.
    Since they are in a circle, ONE is next to TWO and ONE HUNDRED.
    ONE has a sword and kills TWO.
    He passes the sword to THREE who kills FOUR. And so forth.
    NINETY-NINE kills ONE HUNDRED and passes the sword to ONE.
    Then ONE kills THREE and passes the sword to FIVE.
    This goes on until only one person is left standing.
    Which number is he?

    :param i: Number of people in the circle.
    :return: The sole surviving number.
    """
    cir: list[int] = [i for i in range(1, i + 1)]
    pos: int = 0
    while len(cir) > 1:
        pos += 1
        pos %= len(cir)
        del cir[pos]
    print(f"Circle size: {i} - Left standing: {cir[0]}")


def main():
    sword_problem(10)
    sword_problem(100)
    sword_problem(1000)
    sword_problem(10000)


if __name__ == "__main__":
    main()
