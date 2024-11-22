"""
E - 1D Bucket Tool
url: https://atcoder.jp/contests/abc380/tasks/abc380_e
"""

def find_root(node, parents):
    """
    Finds the root of the set containing 'node' with path compression.
    """
    if parents[node] != node:
        parents[node] = find_root(parents[node], parents)
    return parents[node]

num_elements, num_queries = map(int, input().split())

parents = [i for i in range(num_elements + 2)]

groups = [[i, i, i] for i in range(num_elements + 2)]

color_counts = [1] * (num_elements + 1)

for _ in range(num_queries):
    query = list(map(int, input().split()))
    query_type = query[0]

    if query_type == 1: 
        index, new_color = query[1], query[2]
        root = find_root(index, parents)

        left_bound = groups[root][0] - 1
        right_bound = groups[root][1] + 1

        left_root = find_root(left_bound, parents)
        right_root = find_root(right_bound, parents)

        current_color = groups[root][2]
        segment_length = groups[root][1] - groups[root][0] + 1
        color_counts[current_color] -= segment_length
        color_counts[new_color] += segment_length

        groups[root][2] = new_color

        # merge adjacent groups if they have the same color
        if groups[left_root][2] == new_color and groups[right_root][2] == new_color:
            # merge left and right groups
            parents[left_root] = root
            parents[right_root] = root
            groups[root][0] = groups[left_root][0]
            groups[root][1] = groups[right_root][1]
        elif groups[left_root][2] == new_color:
            # only the left group
            parents[left_root] = root
            groups[root][0] = groups[left_root][0]
        elif groups[right_root][2] == new_color:
            # only the right group
            parents[right_root] = root
            groups[root][1] = groups[right_root][1]

    else:  # Query color count
        query_color = query[1]
        print(color_counts[query_color])
