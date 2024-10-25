"""
ABC081B - Shift only
url: https://atcoder.jp/contests/abs/tasks/abc081_b

My explanation: 

Input:
- The input consists of N, the number of integers, followed by a list of integers A.

Loop to Halve:
- We use a while loop to check if all numbers in the list A are even. 
This is done using the condition all(a % 2 == 0 for a in A), which returns True only
if all numbers are divisible by 2 (i.e., even).
- If the condition holds, we halve each number using list comprehension [a // 2 for a in A].
- We increment the operations count each time the numbers are halved.
- The loop terminates when at least one number becomes odd.

Output:
 - Once the loop ends, the value of operations gives the maximum number of times Snuke can perform the operation.
"""
N = int(input())  # number of integers
A = list(map(int, input().split()))  # list of integers

operations = 0

while all(a % 2 == 0 for a in A):  # are numbers even?
    A = [a // 2 for a in A]
    operations += 1

print(operations)

### TEST ###
# input
# 3
# 8 12 40
# output
# 2 (8/2; 12/2; 40/2) -> 2,3,10 but we cannot continue coz there's an odd number
