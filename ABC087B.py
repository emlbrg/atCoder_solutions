"""
ABC087B - Coins
url: https://atcoder.jp/contests/abs/tasks/abc087_b

Problem Statement
You have A 500-yen coins, B 100-yen coins and C 50-yen coins. In how many ways can we select some of these coins so that they are X yen in total?
Coins of the same kind cannot be distinguished. Two ways to select coins are distinguished when, for some kind of coin, the numbers of that coin are different.

Constraints
0≤A,B,C≤50
A+B+C≥1
50≤X≤20 000
A, B and C are integers.
X is a multiple of 50.
"""
A = int(input())  # Number of 500-yen coins
B = int(input())  # Number of 100-yen coins
C = int(input())  # Number of 50-yen coins
X = int(input())  # Total value to achieve

count = 0

# Iterate over the number of 500-yen coins used
for i in range(A + 1):
    for j in range(B + 1):
        # Calculate the remaining value after using i 500-yen coins and j 100-yen coins
        remaining = X - (i * 500 + j * 100)
        
        # Check if the remaining value can be covered by the available 50-yen coins
        if 0 <= remaining <= C * 50 and remaining % 50 == 0:
            count += 1

print(count)

### TEST ###
# 2
# 2
# 2
# 100 -> 2 ?
