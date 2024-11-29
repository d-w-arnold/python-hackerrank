def bigger_is_greater(w: str) -> int:
    """
    Bigger is Greater problem: https://www.hackerrank.com/challenges/bigger-is-greater/problem

    :param w: a word.
    :return: The smallest lexicographically higher string possible or "no answer".
    """
    w: list[str] = list(w)
    i: int = len(w) - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1
    if i >= 0:
        j: int = len(w) - 1
        while w[j] <= w[i]:
            j -= 1
        w[i], w[j] = w[j], w[i]
        return "".join(w[: i + 1] + list(reversed(w[i + 1 :])))
    return "no answer"
