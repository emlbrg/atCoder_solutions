"""
C - Sowing Stones
url: https://atcoder.jp/contests/abc379/tasks/abc379_c
"""
import numpy as np

target_sum, num_elements = map(int, input().split())

elements = np.fromstring(input(), dtype="int64", sep=" ")

count_array = np.fromstring("0 " + input(), dtype="int64", sep=" ")
sorted_indices = np.argsort(elements, kind="stable")
elements = elements[sorted_indices]
count_array[1:] = count_array[1:][sorted_indices]

cumulative_counts = np.cumsum(count_array)

inclusive_diff = cumulative_counts[1:] - elements
exclusive_diff = cumulative_counts[:-1] - elements + 1

if np.any(exclusive_diff < 0) or cumulative_counts[-1] != target_sum:
    print(-1)
    exit()

result = np.sum(inclusive_diff * (inclusive_diff + 1) // 2) - np.sum(exclusive_diff * (exclusive_diff - 1) // 2)

print(result)
