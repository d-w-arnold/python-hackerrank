def breaking_records(scores: list) -> list:
    """
    Breaking the Records problem:
    https://www.hackerrank.com/challenges/three-month-preparation-kit-breaking-best-and-worst-records/problem

    :param scores: Points scored per game.
    :return: An array with the numbers of times she broke her records. Index 0 is for breaking most points records,
    and index 1 is for breaking least points records.
    """
    minimum, maximum, min_total, max_total = scores[0], scores[0], 0, 0
    for score in scores:
        if score > maximum:
            maximum = score
            max_total += 1
        if score < minimum:
            minimum = score
            min_total += 1
    return [max_total, min_total]
