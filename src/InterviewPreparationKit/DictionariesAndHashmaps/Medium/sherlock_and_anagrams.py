from collections import Counter


def sherlock_and_anagrams(s: str) -> int:
    """
    Sherlock and Anagrams problem: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

    :param s: A string.
    :return: The number of unordered anagrammatic pairs of substrings in 's'.
    """
    buckets = {}
    count = 0
    for i in range(0, len(s)):
        for j in range(1, len(s) - i + 1):
            key = frozenset(Counter(s[i:i + j]).items())
            buckets[key] = buckets.get(key, 0) + 1
    for key in buckets:
        count += buckets[key] * (buckets[key] - 1) // 2
    return count
