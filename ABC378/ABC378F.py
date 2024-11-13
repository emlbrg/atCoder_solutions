"""
url: https://atcoder.jp/contests/abc378/tasks/abc378_f
"""
import sys
sys.setrecursionlimit(1000000)

def add_edge():
    N = int(input())
    adj_list = [[] for _ in range(N)]
    
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj_list[u].append(v)
        adj_list[v].append(u)

    def get_degree(node):
        return len(adj_list[node])

    total_pairs = 0
    visited = [False] * N
    
    def explore_tree(node):
        nonlocal total_pairs
        count_of_degree_2 = 0
        
        for neighbor in adj_list[node]:
            if visited[neighbor]:
                continue

            if get_degree(neighbor) == 3:
                visited[neighbor] = True
                explore_tree(neighbor)
            elif get_degree(neighbor) == 2:
                count_of_degree_2 += 1
        
        if count_of_degree_2 > 0:
            total_pairs += count_of_degree_2 * (count_of_degree_2 - 1) // 2

    for node in range(N):
        if not visited[node] and get_degree(node) == 3:
            visited[node] = True
            explore_tree(node)

    print(total_pairs)

add_edge()
