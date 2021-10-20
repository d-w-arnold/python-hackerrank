def components_in_graph(gb: list) -> list:
    """
    Components in a graph problem: https://www.hackerrank.com/challenges/components-in-graph/problem

    :param gb: A 2-d array of integers that represent node ends of graph edges.
    :return: An array with 2 integers, the smallest and largest component sizes.
    """
    nodes_count = 2 * len(gb) + 1
    root = [0] * nodes_count
    count = [0] * nodes_count
    for i in range(1, nodes_count):
        root[i] = i
        count[i] = 1
    for a, b in gb:
        a_root = find_set(a, root)
        b_root = find_set(b, root)
        if a_root == b_root:
            continue
        root[b_root] = a_root
        count[a_root] += count[b_root]
        count[b_root] = 0
    smallest, biggest = nodes_count, -1
    for i in range(1, nodes_count):
        if 1 < count[i]:
            smallest = min(smallest, count[i])
        biggest = max(biggest, count[i])
    return [smallest, biggest]


def find_set(root: int, arr: list) -> int:
    if arr[root] != root:
        return find_set(arr[root], arr)
    return root
