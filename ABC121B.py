"""
B - Can you solve this?
url: https://atcoder.jp/contests/abc121/tasks/abc121_b
"""
def count_solutions(N, M, C, B, A):
    count = 0
    for characteristics in A:
        total = sum(characteristics[j] * B[j] for j in range(M)) + C
        if total > 0:
            count += 1
    return count

N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

result = count_solutions(N, M, C, B, A)
print(result)
