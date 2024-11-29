def how_many_games(p: int, d: int, m: int, s: int) -> int:
    """
    Halloween Sale problem: https://www.hackerrank.com/challenges/halloween-sale/problem

    :param p: the price of the first game.
    :param d: the discount from the previous game price.
    :param m: the minimum cost of a game.
    :param s: the starting budget.
    :return: The number of games that can be bought.
    """
    budget: int = s
    num_of_games: int = 0
    while budget >= p:
        budget -= p
        num_of_games += 1
        p = max(m, p - d)
    return num_of_games
