"""
A - September
url: https://atcoder.jp/contests/abc373/tasks/abc373_a
"""
count = 0

for i in range(1, 13):
    S = input().strip()
    if len(S) == i:
        count += 1

print(count)