def activity_notifications(expenditure: list, d: int) -> int:
    """
    Fraudulent Activity Notifications problem:
    https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

    :param expenditure: Daily expenditures.
    :param d: Days for median spending.
    :return: The number of notices sent.
    """
    f = [0] * 201
    count = 0
    for i in expenditure[:d]:
        f[i] += 1
    for i, v in enumerate(expenditure[d:]):
        limit = get_limit(f, d)
        if v >= limit:
            count += 1
        f[v] += 1
        f[expenditure[i]] -= 1
    return count


def get_limit(f: list, d: int) -> int:
    count = 0
    m1, m2 = (d // 2, d // 2 + 1)
    m = []
    for i, j in enumerate(f):
        count += j
        if not m and m1 <= count:
            m.append(i)
        if m2 <= count:
            m.append(i)
            break
    return m[-1] * 2 if d % 2 else sum(m)
