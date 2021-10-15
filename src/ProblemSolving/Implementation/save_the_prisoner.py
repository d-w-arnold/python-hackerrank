def save_the_prisoner(n: int, m: int, s: int) -> int:
    """
    Save the Prisoner! problem: https://www.hackerrank.com/challenges/save-the-prisoner/problem

    :param n: The number of prisoners.
    :param m: The number of sweets.
    :param s: The chair number to begin passing out sweets from.
    :return: The chair number of the prisoner to warn.
    """
    return (((s - 1) + (m - 1)) % n) + 1
