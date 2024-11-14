"""
A - mod M Game 2
url: https://atcoder.jp/contests/arc185/tasks/arc185_a
"""
import sys 
input = sys.stdin.readline 

t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    s = n*(n + 1) % m 
    f = 0
    if 1 <= s <= n:
            f = 1

    print("Bob" if f else "Alice")