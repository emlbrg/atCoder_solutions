"""
E - How to Win the Election
url: https://atcoder.jp/contests/abc373/tasks/abc373_e
"""
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
les = K - sum(A)

if N == M:
    print(" ".join("0" for _ in range(N)))
    exit()

X = sorted(A)
B = X[-M:]
sum_B = [0 for _ in range(M + 1)]
D = [0 for _ in range(M)]

for i in range(M):
    sum_B[i + 1] = B[i] + sum_B[i]
    D[i] = B[i] * i - sum_B[i]

ans = [-1 for _ in range(N)]

for i in range(N):
    if A[i] < B[0]:
        lef, rgt = -1, M
        while rgt - lef != 1:
            m = (lef + rgt) // 2
            if D[m] + B[m] - A[i] - 1 <= les:
                lef = m
            else:
                rgt = m
        if lef != -1:
            x = (les - D[lef] - B[lef] + A[i] + 1)
            y = x // (lef + 2) + 1
            no = B[lef] + y - 1
            cost = no - A[i]
            if cost <= les:
                ans[i] = cost
    else:
        les -= A[i] - X[-M - 1]
        lef, rgt = -1, M
        while rgt - lef != 1:
            m = (lef + rgt) // 2
            if D[m] + B[m] - A[i] - 1 <= les:
                lef = m
            else:
                rgt = m
        if lef != -1:
            x = (les - D[lef] - B[lef] + A[i] + 1)
            y = x // (lef + 2) + 1
            no = B[lef] + y - 1
            cost = no - A[i]
            if cost <= les:
                ans[i] = max(cost, 0)
        les += A[i] - X[-M - 1]

print(" ".join(map(str, ans)))

