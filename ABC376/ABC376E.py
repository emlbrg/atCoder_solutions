"""
E - Max × Sum
url: https://atcoder.jp/contests/abc376/tasks/abc376_e
"""
from heapq import heappush, heappop

def process_cases():
    _, subset_size = map(int, input().split())
    values_a = list(map(int, input().split()))
    values_b = list(map(int, input().split()))
    paired_values = sorted(zip(values_a, values_b))

    minimum_result = float('inf')
    current_sum = 0
    max_heap = []

    for a_val, b_val in paired_values:
        if len(max_heap) == subset_size - 1:
            minimum_result = min(minimum_result, a_val * (current_sum + b_val))
        heappush(max_heap, -b_val)
        current_sum += b_val
        if len(max_heap) == subset_size:
            current_sum += heappop(max_heap)

    return minimum_result


test_cases = int(input())
print(*[process_cases() for _ in range(test_cases)], sep='\n')

