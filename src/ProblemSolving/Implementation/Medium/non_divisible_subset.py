# Non-Divisible Subset problem: https://www.hackerrank.com/challenges/non-divisible-subset/problem
#
# @param k The divisor.
# @param s An array of integers.
# @return The length of the longest subset of 's' meeting the criteria.
def non_divisible_subset(k: int, s: list):
    d = {x: [] for x in range(k)}
    for i in range(len(s)):
        d[s[i] % k].append(s[i])
    count = 0
    if len(d[0]) > 0:
        count = 1
    listRange = range(1, (k // 2) + 1)
    S = set((x, k - x) for x in listRange)
    for i, j in S:
        if i != j:
            if len(d[i]) > len(d[j]):
                count += len(d[i])
            else:
                count += len(d[j])
        else:
            if len(d[i]) > 0:
                count += 1
    return count
