"""
E - Sum of All Substrings
url: https://atcoder.jp/contests/abc379/tasks/abc379_e
"""

N = int(input())
S = input()

a = [(i + 1) * int(S[i]) for i in range(N)]

for i in range(1, N):
    a[i] += a[i - 1]
    
i = 0
c = 0
ans = []

while i < N or c > 0:
    if i < N:
        c += a[N - 1 - i]
    ans.append(c % 10)
    c //= 10
    i += 1
    
print(*ans[::-1], sep="")