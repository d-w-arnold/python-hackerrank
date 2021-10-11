from collections import Counter


# Count Triplets problem: https://www.hackerrank.com/challenges/count-triplets-1/problem
#
# @param arr An array of integers.
# @param r   The common ratio.
# @return The number of triplets.
def count_triplets(arr: list, r: int):
    a = Counter(arr)
    b = Counter()
    s = 0
    for i in arr:
        j = i // r
        k = i * r
        a[i] -= 1
        if b[j] and a[k] and i % r == 0:
            s += b[j] * a[k]
        b[i] += 1
    return s
