"""
A - Welcome to AtCoder
url: https://atcoder.jp/contests/practice/tasks/practice_1

Problem
Your task is to process some data.
You are given 3 integers a , b , c and a string s. Output result of a+b+c and string s with a half-width break.
"""

a = int(input())  # first integer -> 72
b, c = map(int, input().split())  # second integers -> 128 256
s = input()  # string -> myonmyon

# Calculate the sum of a, b, and c
total = a + b + c

print(f'{total} {s}')

### TEST ###
# 72
# 128 256
# myonmyon