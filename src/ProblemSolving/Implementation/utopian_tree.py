def utopian_tree(n: int):
    """
    Utopian Tree problem: https://www.hackerrank.com/challenges/utopian-tree/problem

    :param n: The number of growth cycles to simulate.
    :return: The height of the tree after the given number of cycles.
    """
    if n <= 0:
        return 1
    height = 1
    for i in range(0, n):
        if i % 2 == 0:
            height *= 2
        else:
            height += 1
    return height
