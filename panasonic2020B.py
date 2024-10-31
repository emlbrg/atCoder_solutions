"""
B - Bishop
url: https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_b
"""
h, w = map(int, input().split())
ans = 0
if h == 1 or w == 1:
    ans = 1
elif h % 2 == 0:
    ans = h // 2 * w
elif w % 2 == 0:
    ans = w // 2 * h
else:
    ans = (h-1) // 2 * w + (w+1) // 2

print(ans)

