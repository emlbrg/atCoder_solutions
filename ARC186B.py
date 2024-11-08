"""
url: https://atcoder.jp/contests/arc186/tasks/arc186_b
"""
from sys import setrecursionlimit
import bisect

setrecursionlimit(10**8)
MOD = 998244353

n = int(input())
elements = list(map(int, input().split()))
for i in range(n):
    elements[i] -= 1

# Precompute factorials
factorial = [1]
for i in range(1, 3 * 10**5 + 2):
    factorial.append(factorial[-1] * i % MOD)

def combination(a, b):
    if a < b:
        return 0
    return factorial[a] * pow(factorial[b], -1, MOD) * pow(factorial[a - b], -1, MOD) % MOD

# Organize elements by index
index_map = [[] for _ in range(n)]  # type: ignore
for i in range(n):
    index_map[elements[i]].append(i)

# Recursive function for calculation
def calculate(left, right):
    if left == right:
        return 1
    mid_index = index_map[left - 1][bisect.bisect(index_map[left - 1], right) - 1]
    
    if mid_index == left:
        return calculate(left + 1, right)
    if mid_index == right:
        return calculate(left, right - 1)
    
    result = calculate(left, mid_index - 1) * calculate(mid_index + 1, right) % MOD
    result = result * combination(right - left, right - mid_index) % MOD
    return result

print(calculate(0, n - 1) % MOD)
