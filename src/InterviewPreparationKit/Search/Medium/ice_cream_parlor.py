def what_flavors(cost: list, money: int):
    """
    Hash Tables: Ice Cream Parlor problem: https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem

    :param cost: The prices for each flavor.
    :param money: The amount of money they have to spend.
    """
    freq_map = {}
    for i in range(0, len(cost)):
        c = cost[i]
        n = money - c
        if n in freq_map:
            print(freq_map[n][0], (i + 1))
        elif c in freq_map:
            freq_map[c].append(i + 1)
        else:
            freq_map[c] = [i + 1]
