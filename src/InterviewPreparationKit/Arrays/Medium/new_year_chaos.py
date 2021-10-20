def min_bribes(q: list) -> None:
    """
    New Year Chaos problem: https://www.hackerrank.com/challenges/new-year-chaos/problem

    :param q: The positions of the people after all bribes.
    """
    total = 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                total += 1
    print(total)
