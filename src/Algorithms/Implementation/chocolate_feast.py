def chocolate_feast(n: int, c: int, m: int) -> int:
    """
    Chocolate Feast problem: https://www.hackerrank.com/challenges/chocolate-feast/problem

    :param n: Bobby's initial amount of money.
    :param c: the cost of a chocolate bar.
    :param m: the number of wrappers he can turn in for a free bar.
    :return: The number of chocolates Bobby can eat after taking full advantage of the promotion.
    """
    budget: int = n
    num_of_choc: int = 0
    num_of_wrappers: int = 0
    while budget >= c:
        more: int = int(budget / c)
        budget = budget % c
        num_of_choc += more
        num_of_wrappers += more
        if num_of_wrappers >= m:
            budget = c * int(num_of_wrappers / m)
            num_of_wrappers = num_of_wrappers % m
    return num_of_choc
