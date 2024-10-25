"""
ABC086A - Product
url:https://atcoder.jp/contests/abs/tasks/abc086_a

Problem Statement
AtCoDeer the deer found two positive integers, a and b. Determine whether the product of a and b is even or odd.

Constraints
1 ≤ a,b ≤ 10000
a and b are integers.

Input
Input is given from Standard Input in the following format:
a b

Output
If the product is odd, print `Odd`; if it is even, print `Even`.
"""
a, b = map(int, input().split())

if (a * b) % 2 == 0:
    print('Even')
else:
    print('Odd')


### TEST ###
# 3 4
# out Even