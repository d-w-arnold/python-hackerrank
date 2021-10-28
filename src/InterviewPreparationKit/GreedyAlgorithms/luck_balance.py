def luck_balance(k: int, contests: list) -> int:
    """
    Luck Balance problem: https://www.hackerrank.com/challenges/luck-balance/problem

    :param k: The number of important contests Lena can lose.
    :param contests: A 2D array of integers where each contests[i] contains two integers that represent the luck balance and importance of the ith contest.
    :return: The maximum luck balance achievable.
    """
    total = 0
    contests = sorted([(i[0], i[1]) for i in contests], key=lambda contest: (contest[1], contest[0]), reverse=True)
    for luck, v in contests:
        if v == 0:
            total += luck
        elif k > 0:
            total += luck
            k -= 1
        else:
            total -= luck
    return total
