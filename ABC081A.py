"""
ABC081A - Placing Marbles
url: https://atcoder.jp/contests/abs/tasks/abc081_a

Problem Statement
Snuke has a grid consisting of three squares numbered 1, 2 and 3. 
In each square, either 0 or 1 is written. The number written in Square i is si.
Snuke will place a marble on each square that says 1. Find the number of squares on which Snuke will place a marble.

Constraints
Each of s1, s2, and s3 is either 1 or 0.

Input
Input is given from Standard Input in the following format:
s1s2s3

Output
Print the answer.
"""
# honestly this problem definition was needlessly convoluted wth
s = input()

marble_count = s.count('1')  # if I understand correctly, 1 means we put the marble

print(marble_count)

### TEST ###
# 101 -> 2
# 000 -> 0
