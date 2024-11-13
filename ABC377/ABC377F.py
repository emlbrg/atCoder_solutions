"""
F - Avoid Queen Attack
url: https://atcoder.jp/contests/abc377/tasks/abc377_f
"""
# I dont play chess so fingers crossed lol
N, M = map(int, input().split())
rows, cols, diag_diff, diag_sum = set(), set(), set(), set()

for _ in range(M):
    x, y = map(int, input().split())
    rows.add(x)
    cols.add(y)
    diag_diff.add(x - y)
    diag_sum.add(x + y)

unrestricted = (N - len(rows)) * (N - len(cols))

for d in diag_diff:
    count = N - abs(d)
    count -= sum(1 for row in rows if 1 <= row - d <= N)
    count -= sum(1 for col in cols if 1 <= col + d <= N)
    count += sum(1 for row in rows if (row - d) in cols and 1 <= row - d <= N)
    unrestricted -= count

for s in diag_sum:
    if 2 <= s <= N + 1:
        count = s - 1
    elif N + 2 <= s <= 2 * N:
        count = 2 * N + 1 - s
    else:
        count = 0

    count -= sum(1 for row in rows if 1 <= s - row <= N)
    count -= sum(1 for col in cols if 1 <= s - col <= N)
    count += sum(1 for row in rows if (s - row) in cols and 1 <= s - row <= N)
    unrestricted -= count

for d in diag_diff:
    for s in diag_sum:
        if (d + s) % 2 == 0:
            row = (d + s) // 2
            col = (s - d) // 2
            if 1 <= row <= N and 1 <= col <= N and row not in rows and col not in cols:
                unrestricted += 1

print(unrestricted)
