def min_abs_diff(arr: list) -> int:
    """
    Minimum Absolute Difference in an Array problem: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

    :param arr: An array of integers.
    :return: The minimum absolute difference found.
    """
    arr.sort()
    ans = abs(arr[0] - arr[1])
    for i in range(0, len(arr) - 1):
        ans = min(ans, abs(arr[i] - arr[i + 1]))
    return ans
