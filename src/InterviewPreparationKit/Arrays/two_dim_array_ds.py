import sys


def hourglass_sum(arr: list) -> int:
    """
    Hour Glass Sum problem: https://www.hackerrank.com/challenges/2d-array/problem

    :param arr: An array of integers.
    :return: The maximum hourglass sum.
    """
    largest_sum = -sys.maxsize
    for i in range(0, len(arr[0]) - 2):
        for j in range(0, len(arr) - 2):
            largest_sum = max(largest_sum, sum_two_dim_array(get_hour_glass(arr, i, j)))
    return largest_sum


def get_hour_glass(arr: list, x: int, y: int) -> list:
    if x >= len(arr[0]) or y >= len(arr):
        return []
    return [[arr[x][y + i] for i in range(0, 3)], [0, arr[x + 1][y + 1], 0], [arr[x + 2][y + i] for i in range(0, 3)]]


def sum_two_dim_array(two_dim_array: list) -> int:
    total = 0
    for i in two_dim_array:
        for j in i:
            total += j
    return total
