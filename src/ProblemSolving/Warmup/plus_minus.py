def plus_minus(arr: list) -> None:
    """
    Plus Minus problem: https://www.hackerrank.com/challenges/plus-minus/problem

    :param arr: An array of integers.
    """
    pos_num = neg_num = zeros = 0
    for i in arr:
        if i > 0:
            pos_num += 1
        elif i < 0:
            neg_num += 1
        else:
            zeros += 1
    print(f"{pos_num / len(arr):.6f}")
    print(f"{neg_num / len(arr):.6f}")
    print(f"{zeros / len(arr):.6f}")
