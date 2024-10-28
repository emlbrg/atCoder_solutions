"""
C - Separated Lunch
url: https://atcoder.jp/contests/abc374/tasks/abc374_c

KEYENCE headquarters have N departments, and the number of people in the i-th department
(1≤i≤N) is Ki.
When assigning each department to Group A or Group B, having each group take
lunch breaks at the same time, and ensuring that the lunch break times of Group A
and Group B do not overlap, find the minimum possible value of the maximum number
of people taking a lunch break at the same time.
In other words, find the minimum possible value of the larger of the following: 
the total number of people in departments assigned to Group A, and the total number.

Constraints
2≤N≤20
1≤Ki≤10^8
 
All input values are integers.of people in departments assigned to Group B.

Input
The input is given from Standard Input in the following format:

N
K1 K2… KN
​
Output
Print the minimum possible value of the maximum number of people taking a lunch break at the same time.
"""
def minimize_max_lunch_break(N, departments):
    total_people = sum(departments)
    half_people = total_people // 2
    min_max = total_people  # from max of all people 

    def backtrack(index, group_a_sum):
        nonlocal min_max
        
        if index == N:
            group_b_sum = total_people - group_a_sum
            current_max = max(group_a_sum, group_b_sum)
            min_max = min(min_max, current_max)
            return
        
        backtrack(index + 1, group_a_sum + departments[index])

        backtrack(index + 1, group_a_sum)

    backtrack(0, 0)
    return min_max

n = int(input().strip())
departments = list(map(int, input().strip().split()))

result = minimize_max_lunch_break(n, departments)
print(result)