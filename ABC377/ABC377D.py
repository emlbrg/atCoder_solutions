"""
D - Many Segments 2
url: https://atcoder.jp/contests/abc368/tasks/abc368_d
"""
num_intervals, max_range = map(int, input().split())

range_limits = [1] * (max_range + 1)

for _ in range(num_intervals):
    left, right = map(int, input().split())
    range_limits[right] = max(range_limits[right], left + 1)

for i in range(1, max_range + 1):
    range_limits[i] = max(range_limits[i], range_limits[i - 1])

total_valid_points = 0
for i in range(1, max_range + 1):
    total_valid_points += i - range_limits[i] + 1

print(total_valid_points)
