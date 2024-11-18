"""
C - Make Isomorphic
url: https://atcoder.jp/contests/abc371/tasks/abc371_c
"""
# Simple undirected path?
# CHECK THIS What does it mean for graphs to be isomorphic?
from itertools import permutations

num_vertices = int(input())
graph_G = [[False] * num_vertices for _ in range(num_vertices)]

num_edges_G = int(input())
for _ in range(num_edges_G):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph_G[u][v] = True
    graph_G[v][u] = True

graph_H = [[False] * num_vertices for _ in range(num_vertices)]

num_edges_H = int(input())
for _ in range(num_edges_H):
    u, v = map(int, input().split())
    u -= 1
    graph_H[u][v] = True
    graph_H[v][u] = True

cost_matrix = [[-1] * num_vertices for _ in range(num_vertices)]
for i in range(num_vertices - 1):
    row = list(map(int, input().split()))
    for j in range(i + 1, num_vertices):
        cost_matrix[i][j] = row[j - (i + 1)]
        cost_matrix[j][i] = row[j - (i + 1)]

min_cost = float('inf')

for perm in permutations(range(num_vertices)):
    current_cost = 0

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph_G[i][j] != graph_H[perm[i]][perm[j]]:
                current_cost += cost_matrix[perm[i]][perm[j]]

    min_cost = min(min_cost, current_cost)

print(min_cost)  # RE????
