def get_min_cost(k: int, c: list) -> int:
    """
    Greedy Florist problem: https://www.hackerrank.com/challenges/greedy-florist/problem

    :param k: The number of friends.
    :param c: The original price of each flower.
    :return: The minimum cost to purchase all flowers.
    """
    c.sort()
    total, num_of_purchases, num_of_group_purchases = 0, 0, -1
    for i in range(len(c) - 1, -1, -1):
        if num_of_purchases % k == 0:
            num_of_group_purchases += 1
        num_of_purchases += 1
        total += (num_of_group_purchases + 1) * c[i]
    return total
