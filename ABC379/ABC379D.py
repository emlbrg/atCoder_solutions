"""
D - Home Garden
url: https://atcoder.jp/contests/abc379/tasks/abc379_d
"""

from collections import deque

num_queries = int(input())
active_pots = deque()  # type: ignore
elapsed_days = [0] * num_queries
results = []

for query_index in range(num_queries):
    query = list(map(int, input().split()))
    elapsed_days[query_index] = elapsed_days[query_index - 1]
    
    if query[0] == 1:
        active_pots.append(query_index)
    elif query[0] == 2:
        elapsed_days[query_index] += query[1]
    elif query[0] == 3:
        threshold = query[1]
        removed_count = 0
        while active_pots and elapsed_days[query_index] - elapsed_days[active_pots[0]] >= threshold:
            active_pots.popleft()
            removed_count += 1
        results.append(removed_count)

print(*results, sep='\n')
