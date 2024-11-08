"""
url: https://atcoder.jp/contests/abc368/tasks/abc368_d
"""
num_nodes, num_targets = map(int, input().split())

tree = [set() for _ in range(num_nodes)]  # type: ignore

for _ in range(num_nodes - 1):
    node1, node2 = map(int, input().split())
    node1 -= 1
    node2 -= 1
    tree[node1].add(node2)
    tree[node2].add(node1)

target_vertices = set(int(x) - 1 for x in input().split())

degrees = [len(connections) for connections in tree]
leaves = [idx for idx, deg in enumerate(degrees) if deg == 1]

remaining_nodes = num_nodes
for leaf in leaves:
    if leaf in target_vertices:
        continue
    neighbor = tree[leaf].pop()
    tree[neighbor].remove(leaf)
    remaining_nodes -= 1
    if len(tree[neighbor]) == 1:
        leaves.append(neighbor)

print(remaining_nodes)

