def solve(arr: list) -> int:
    """
    Find Maximum Index Product problem: https://www.hackerrank.com/challenges/find-maximum-index-product/problem

    :param arr: An array of integers.
    :return: The maximum IndexProduct(i) among all i.
    """
    ans = -1
    left = next_greater_in_left(arr)
    right = next_greater_in_right(arr)
    for i in range(1, len(arr) + 1):
        ans = max(ans, left[i] * right[i])
    return ans


def next_greater_in_left(arr: list) -> list:
    index = [0] * (len(arr) + 1)
    s = []
    for i in range(len(arr) - 1, -1, -1):
        build_index(arr, index, s, i)
    return index


def next_greater_in_right(arr: list) -> list:
    index = [0] * (len(arr) + 1)
    s = []
    for i in range(0, len(arr)):
        build_index(arr, index, s, i)
    return index


def build_index(a: list, index: list, s: list, i: int) -> None:
    while s and a[i] > a[s[-1] - 1]:
        r = s[-1]
        s.pop()
        index[r - 1] = i + 1
    s.append(i + 1)
