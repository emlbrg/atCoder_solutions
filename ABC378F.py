"""
url: https://atcoder.jp/contests/abc378/tasks/abc378_f
"""
import sys
sys.setrecursionlimit(1000000)

def add_edge():
    # Read number of nodes
    N = int(input())
    adj_list = [[] for _ in range(N)]
    
    # Read the edges and construct the graph (0-based indexing)
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Helper function to return the degree of a node
    def get_degree(node):
        return len(adj_list[node])

    # Variables to track the result
    total_pairs = 0
    visited = [False] * N
    
    # Depth-first search to explore the tree
    def explore_tree(node):
        nonlocal total_pairs
        count_of_degree_2 = 0
        
        # Explore all neighbors
        for neighbor in adj_list[node]:
            if visited[neighbor]:
                continue

            # If the node has degree 3, continue DFS
            if get_degree(neighbor) == 3:
                visited[neighbor] = True
                explore_tree(neighbor)
            # If the node has degree 2, increase the count
            elif get_degree(neighbor) == 2:
                count_of_degree_2 += 1
        
        # After finishing exploring a node, calculate pairs
        if count_of_degree_2 > 0:
            total_pairs += count_of_degree_2 * (count_of_degree_2 - 1) // 2

    # Traverse all nodes
    for node in range(N):
        if not visited[node] and get_degree(node) == 3:
            visited[node] = True
            explore_tree(node)
    
    # Output the final result
    print(total_pairs)

add_edge()
