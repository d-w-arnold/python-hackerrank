def kangaroo(x1: int, v1: int, x2: int, v2: int):
    """
    Number Line Jumps problem: https://www.hackerrank.com/challenges/kangaroo/problem

    :param x1: Starting position for kangaroo 1.
    :param v1: Jump distance for kangaroo 1.
    :param x2: Starting position for kangaroo 2.
    :param v2: Jump distance for kangaroo 2.
    :return: Either YES or NO.
    """
    yes = "YES"
    no = "NO"
    if v1 == v2:
        return yes if x1 == x2 else no
    elif x1 == x2:
        return no
    elif x1 > x2:
        return yes if same_location_possible(x1, v1, x2, v2) else no
    else:
        return yes if same_location_possible(x2, v2, x1, v1) else no


def same_location_possible(lead_start: int, lead_jump: int, tail_start: int, tail_jump: int):
    if lead_jump <= tail_jump:
        lead_pos = lead_start
        tail_pos = tail_start
        diff = lead_start - tail_start
        while True:
            if diff <= 0:
                return diff == 0
            lead_pos += lead_jump
            tail_pos += tail_jump
            diff = lead_pos - tail_pos
    return False
