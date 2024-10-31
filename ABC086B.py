"""
B - 1 21
url: https://atcoder.jp/contests/abc086/tasks/abc086_b
"""
import math

def is_square_number_concatenation(a, b):
    n = int(str(a) + str(b))  # concatenate! and make into int
    
    root = math.isqrt(n)
    if root * root == n:
        return "Yes"
    else:
        return "No"

a, b = map(int, input().split())

print(is_square_number_concatenation(a, b))
