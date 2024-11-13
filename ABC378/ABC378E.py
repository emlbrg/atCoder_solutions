"""
E - Mod Sigma Problem
url: https://atcoder.jp/contests/abc378/tasks/abc378_e
"""
# I think this is a Binary Indexed Tree problem and I hate it
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def query(self, idx):
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & -idx
        return total

    def update(self, idx, value):
        while idx <= self.n:
            self.tree[idx] += value
            idx += idx & -idx

N, M = map(int, input().split())
array = list(map(int, input().split()))

prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i + 1] = (prefix_sum[i] + array[i]) % M

fenwick = FenwickTree(M)
result = 0
cumulative_sum = 0
fenwick.update(1, 1)

for i in range(1, N + 1):
    current_sum = prefix_sum[i]
    count_less = fenwick.query(current_sum + 1)
    count_more = i - count_less
    result += current_sum * i - cumulative_sum + M * count_more
    cumulative_sum += current_sum
    fenwick.update(current_sum + 1, 1)

print(result)
