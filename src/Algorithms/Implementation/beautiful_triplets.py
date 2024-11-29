def beautiful_triplets(d: int, arr: list[int]) -> int:
    """
    Beautiful Triplets problem: https://www.hackerrank.com/challenges/beautiful-triplets/problem

    :param d: the value to match.
    :param arr: the sequence, sorted ascending.
    :return: The number of beautiful triplets.
    """
    indexes_sep_d: dict[int, list[int]] = {}
    for i, n in enumerate(arr):
        pointer: int = i
        while True:
            pointer += 1
            if pointer >= len(arr):
                break
            lookup_n: int = arr[pointer]
            if lookup_n - n < d:
                continue
            elif lookup_n - n > d:
                break
            elif i in indexes_sep_d:
                indexes_sep_d[i].append(pointer)
            else:
                indexes_sep_d[i] = [pointer]
    num_of_bts: int = 0
    for k, v in indexes_sep_d.items():
        for i in v:
            if meta := indexes_sep_d.get(i):
                num_of_bts += len(meta)
    return num_of_bts
