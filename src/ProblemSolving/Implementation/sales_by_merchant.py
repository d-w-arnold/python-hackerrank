def sock_merchant(n: int, ar: list) -> int:
    """
    Sales by Match problem: https://www.hackerrank.com/challenges/sock-merchant/problem

    :param n: The number of socks in the pile.
    :param ar: The colors of each sock.
    :return: The number of pairs.
    """
    pairs = 0
    socks = {}
    for i in range(0, n):
        a = ar[i]
        if a in socks:
            value = socks[a]
            if value % 2 == 1:
                pairs += 1
            socks[a] = value + 1
        else:
            socks[a] = 1
    return pairs
