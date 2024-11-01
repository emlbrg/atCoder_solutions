"""
A - Takahashi san 2
url: https://atcoder.jp/contests/abc374/tasks/abc374_a

Problem Statement
KEYENCE has a culture of addressing everyone with the suffix "-san," regardless of roles, age, or positions.

You are given a string S consisting of lowercase English letters.
If S ends with san, print Yes; otherwise, print No.

Constraints
S is a string of length between 4 and 30, inclusive, consisting of lowercase English letters.
Input
The input is given from Standard Input in the following format:
S

Output
If S ends with san, print Yes; otherwise, print No.
"""
s = input().strip()

if s.endswith('san'):
    print('Yes')
else:
    print('No')

