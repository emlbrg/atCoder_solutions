"""
C - Rally
url: https://atcoder.jp/contests/abc156/tasks/abc156_c

Problem Statement
There are N people living on a number line.

The i-th person lives at coordinate Xi.

You are going to hold a meeting that all N people have to attend.

The meeting can be held at any integer coordinate. If you choose to hold the meeting at coordinate P, the i-th person will spend (Xi−P)^2 points of stamina to attend the meeting.

Find the minimum total points of stamina the N people have to spend.

Constraints
All values in input are integers.
1≤N≤100
1≤X 
i≤100

Input
Input is given from Standard Input in the following format:

N
X1 X2... XN
​
Output
Print the minimum total stamina the N people have to spend.

Example:
Input
2
1 4

Output

5

Explanation:
Assume the meeting is held at coordinate 2. In this case, the first person will spend (1−2)^2=1 points of stamina, and the second person will spend (4−2)^2=4 points of stamina, for a total of 5 points of stamina.
This is the minimum total stamina that the 2 people have to spend.

Note that you can hold the meeting only at an integer coordinate.
"""
def min_total_stamina(n: int, positions: list) -> int:
    min_stamina = 10**9  # Start with a large number as we are minimizing
    for p in range(1, 101):  # i≤100
        stamina_spent = 0
        for x in positions:
            stamina_spent += (x - p) ** 2  # stamina for each person
        min_stamina = min(min_stamina, stamina_spent)
    return min_stamina

n = int(input())  # N people living on a number line
positions = list(map(int, input().split()))  # The X in the problem def

print(min_total_stamina(n, positions))