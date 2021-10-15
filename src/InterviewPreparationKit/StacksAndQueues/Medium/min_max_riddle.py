def riddle(arr: list) -> list:
    """
    Min Max Riddle problem: https://www.hackerrank.com/challenges/min-max-riddle/problem

    :param arr: An array of 'n' integers.
    :return: An array of integers representing the maximum minimum value for each window size from 1 to 'n'.
    """
    n = len(arr)
    s = []
    left = ([-1] * n) + [0]
    right = ([n] * n) + [0]
    for i in range(0, n):
        while s and arr[s[-1]] >= arr[i]:
            s.pop()
        if s:
            left[i] = s[-1]
        s.append(i)
    while s:
        s.pop()
    for i in range(n - 1, -1, -1):
        while s and arr[s[-1]] >= arr[i]:
            s.pop()
        if s:
            right[i] = s[-1]
        s.append(i)
    max_min = [0] * (n + 1)
    for i in range(0, n):
        ln = right[i] - left[i] - 1
        max_min[ln] = max(max_min[ln], arr[i])
    for i in range(n - 1, 0, -1):
        max_min[i] = max(max_min[i], max_min[i + 1])
    return max_min[1:]
