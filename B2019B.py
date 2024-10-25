"""
B - Tax Rate
url: https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b

Problem Statement
Takahashi bought a piece of apple pie at ABC Confiserie. 
According to his memory, he paid N yen for it.
The consumption tax rate for foods in this shop is 8 percent. That is, to buy an apple pie priced at X yen before tax, you have to pay X*1.08 yen (rounded down to the nearest integer).
Takahashi forgot the price of his apple pie before tax, X, and wants to know it again. Write a program that takes N as input and finds X. We assume X is an integer.
If there are multiple possible values for X, find any one of them. Also, Takahashi's memory of N, the amount he paid, may be incorrect. If no value could be X, report that fact.

Constraints
1≤N≤50000
N is an integer.

Input
Input is given from Standard Input in the following format:
N

Output
If there are values that could be X, the price of the apple pie before tax, print any one of them.
If there are multiple such values, printing any one of them will be accepted.
If no value could be X, print :(
"""
import math 

n = int(input())
x = math.ceil(n / 1.08)
# print(x)
if math.floor(x * 1.08) == n:
    print(x)
else:
    print(':(')