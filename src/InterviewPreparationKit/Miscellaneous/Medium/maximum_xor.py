def max_xor(arr: list, queries: list):
    """
    Maximum Xor problem: https://www.hackerrank.com/challenges/maximum-xor/problem

    :param arr: An array of integers.
    :param queries: An array of integers to query.
    :return: An array of integers, each representing the maximum xor value for each
    element queries[j] against all elements of arr.
    """
    ans = []
    trie = {}
    k = len(bin(max(arr + queries))) - 2
    for number in ['{:b}'.format(x).zfill(k) for x in arr]:
        node = trie
        for char in number:
            node = node.setdefault(char, {})
    for n in queries:
        node = trie
        s = ''
        for char in '{:b}'.format(n).zfill(k):
            tmp = str(int(char) ^ 1)
            tmp = tmp if tmp in node else char
            s += tmp
            node = node[tmp]
        ans.append(int(s, 2) ^ n)
    return ans
