"""
D - Hidden Weights
url: https://atcoder.jp/contests/abc373/tasks/abc373_d
"""
import sys

input = sys.stdin.readline

num_vertices, num_edges = map(int, input().split())
graph = [[] for _ in range(num_vertices)]  # type: ignore

for _ in range(num_edges):
    from_vertex, to_vertex, weight = map(int, input().split())
    from_vertex -= 1  # convert to zero-based index
    to_vertex -= 1    # convert to zero-based index
    graph[from_vertex].append((to_vertex, weight))
    graph[to_vertex].append((from_vertex, -weight))

visited_nodes = [False] * num_vertices
result = [0] * num_vertices

def depth_first_search(vertex):
    stack = [vertex]
    while stack:
        current = stack.pop()
        for neighbor, weight in graph[current]:
            if not visited_nodes[neighbor]:
                visited_nodes[neighbor] = True
                result[neighbor] = result[current] + weight
                stack.append(neighbor)

for vertex in range(num_vertices):
    if not visited_nodes[vertex]:
        visited_nodes[vertex] = True
        depth_first_search(vertex)

print(" ".join(map(str, result)))
