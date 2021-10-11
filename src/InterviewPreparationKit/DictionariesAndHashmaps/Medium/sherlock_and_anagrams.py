from collections import Counter


# Sherlock and Anagrams problem: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
#
# @param s A string.
# @return The number of unordered anagrammatic pairs of substrings in 's'.
def sherlock_and_anagrams(s: str):
    buckets = {}
    count = 0
    for i in range(len(s)):
        for j in range(1, len(s) - i + 1):
            key = frozenset(Counter(s[i:i + j]).items())  # O(N) time key extract
            buckets[key] = buckets.get(key, 0) + 1
    for key in buckets:
        count += buckets[key] * (buckets[key] - 1) // 2
    return count
