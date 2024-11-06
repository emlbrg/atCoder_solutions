"""
A - Candy Button
url: https://atcoder.jp/contests/abc376/tasks/abc376_a
"""
def count_candies(N, C, T):
    candies = 1
    last_received_time = T[0]

    for i in range(1, N):
        if T[i] - last_received_time >= C:
            candies += 1
            last_received_time = T[i]
    
    return candies

N, C = map(int, input().split())
T = list(map(int, input().split()))

print(count_candies(N, C, T))
