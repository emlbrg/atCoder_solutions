"""
B - Collecting Balls (Easy Version)
url: https://atcoder.jp/contests/abc074/tasks/abc074_b
"""
N = int(input().strip())  # no of balls
K = int(input().strip())  # X of B robot
x = list(map(int, input().strip().split()))  # Xvof the balls

total_min_distance = 0

for i in range(N):
    distance_A = 2 * x[i]
    distance_B = 2 * (K - x[i])
    total_min_distance += min(distance_A, distance_B)

print(total_min_distance)

