def minimum_distance(a: list[int]) -> int:
    """
    Minimum Distance problem: https://www.hackerrank.com/challenges/minimum-distances/problem

    :param a: An array of integers.
    :return: The minimum distance.
    """
    ans: int = None
    last_known_positions: dict[int, int] = {}
    for i, n in enumerate(a):
        if n in last_known_positions:
            diff = i - last_known_positions[n]
            ans = diff if ans is None else min(diff, ans)
        else:
            last_known_positions[n] = i
    if ans is None:
        return -1
    return ans
