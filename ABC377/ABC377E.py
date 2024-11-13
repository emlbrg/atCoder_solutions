"""
E - Permute K times 2
url: https://atcoder.jp/contests/abc377/tasks/abc377_e
"""
import sys
import threading

def solve_permutation():
    sys.setrecursionlimit(1 << 25)
    n, shifts = map(int, sys.stdin.readline().split())
    permutation = list(map(int, sys.stdin.readline().split()))
    permutation = [p - 1 for p in permutation]

    is_visited = [False] * n
    transformed = [0] * n

    for start in range(n):
        if not is_visited[start]:
            # Construct cycle starting from 'start'
            cycle_nodes = []
            current_node = start
            while not is_visited[current_node]:
                is_visited[current_node] = True
                cycle_nodes.append(current_node)
                current_node = permutation[current_node]

            cycle_length = len(cycle_nodes)
            shift_steps = pow(2, shifts, cycle_length)

            for index in range(cycle_length):
                new_position = (index + shift_steps) % cycle_length
                transformed[cycle_nodes[index]] = cycle_nodes[new_position]

    transformed = [x + 1 for x in transformed]
    print(' '.join(map(str, transformed)))

threading.Thread(target=solve_permutation).start()
