"""
D - Cycle
url: https://atcoder.jp/contests/abc376/tasks/abc376_d
"""
from collections import deque

# Read inputs
node_count, edge_count = map(int, input().split())
connections = [[] for _ in range(node_count)]  # type: ignore

# Build the adjacency list
for _ in range(edge_count):
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    connections[start].append(end)

# Initialize distance array and queue
MAX_DIST = 10 ** 10
distances = [MAX_DIST] * node_count
queue = deque([(0, -1, 0)])

# Breadth-first search to find shortest path
while queue:
    current, previous, steps = queue.popleft()
    if distances[current] < steps:
        continue
    for neighbor in connections[current]:
        if distances[neighbor] > steps + 1:
            distances[neighbor] = steps + 1
            queue.append((neighbor, current, steps + 1))

# Output the result
if distances[0] == MAX_DIST:
    print(-1)
else:
    print(distances[0])
