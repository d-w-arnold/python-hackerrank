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
    game_price: int = p
    while budget >= game_price:
        budget -= game_price
        num_of_games += 1
        game_price = max(m, game_price - d)
    return num_of_games
