def sub_str_count(n: int, s: str) -> int:
    """
    Special String Again problem: https://www.hackerrank.com/challenges/special-palindrome-again/problem

    :param n: The length of string s.
    :param s: A string.
    :return: The number of special substrings.
    """
    ans = count = 0
    lst = []
    cur = None
    for i in range(0, n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                lst.append((cur, count))
            cur = s[i]
            count = 1
    lst.append((cur, count))
    for i in lst:
        ans += (i[1] * (i[1] + 1)) // 2
    for i in range(1, len(lst) - 1):
        if lst[i][1] == 1 and lst[i - 1][0] == lst[i + 1][0]:
            ans += min(lst[i - 1][1], lst[i + 1][1])
    return ans
