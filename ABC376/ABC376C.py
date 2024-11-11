"""
C - Prepare Another Box
ur: https://atcoder.jp/contests/abc376/tasks/abc376_c
"""
n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))

ans = 0

# Try to replace elements in `b` with elements from `a`
for i in range(n - 1, 0, -1):
    if a[i] > b[i - 1]:
        b.insert(i, a[i])
        ans = a[i]
        break
else:
    b.insert(0, a[0])
    ans = a[0]

for i in range(n):
    if a[i] > b[i]:
        print(-1)
        break
else:
    print(ans)

