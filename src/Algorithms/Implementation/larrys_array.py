def larrys_array(A: list[int]) -> int:
    """
    Larry's Array problem: https://www.hackerrank.com/challenges/larrys-array/problem

    :param A: an array of integers
    :return: Either "YES" or "NO".
    """
    c = 0
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                c += 1
    if c % 2 == 0:
        return "YES"
    return "NO"
