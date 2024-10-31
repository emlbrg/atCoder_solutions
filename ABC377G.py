"""
G - Edit to Match
url: https://atcoder.jp/contests/abc377/tasks/abc377_g
"""
N = int(input())
A, INF = 26, 10**9
a = ord("a")
t = [[-1] * A]
d = [0]
for _ in range(N):
    S = input()
    l = len(S)
    v, ans = 0, l
    for i in range(l):
        if t[v][ord(S[i]) - a] == -1:
            t.append([-1] * A)
            t[v][ord(S[i]) - a] = len(t) - 1
            d.append(INF)
        v = t[v][ord(S[i]) - a]
        ans = min(ans, d[v] + l - i - 1)
        d[v] = min(d[v], l - i - 1)
    print(ans)
