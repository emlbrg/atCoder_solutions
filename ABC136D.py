"""
D - Gathering Children
url: https://atcoder.jp/contests/abc136/tasks/abc136_d

Problem Breakdown
Initial Setup:
- Each character in the string S corresponds to a square.
- The leftmost square always has an 'R', and the rightmost square always has an 'L'.
- Children start on each square, meaning initially, there is one child on each square.

Movement Instructions:
- If a child is on a square with 'R', they will move one square to the right.
- If a child is on a square with 'L', they will move one square to the left.
- The problem states that each child will perform their moves up to 10^100 times, which is an enormous number.

Understanding Movement Dynamics:
Since the children are continually moving based on the characters, their movement will eventually stabilize.
This means that after a certain number of moves, no child will change their position anymore.
"""
def final_positions(S: str):
    n = len(S)
    result = [0] * n

    for i in range(n):
        if S[i] == 'R':
            # If the character is 'R', this child will move to the right
            result[i] += 1  # Start from the current position
            if i + 1 < n:
                result[i + 1] += result[i]  # Move to the right position
        elif S[i] == 'L':
            # If the character is 'L', children will be moved to the left
            if i - 1 >= 0:
                result[i - 1] += result[i]  # Move to the left position

    return result

S = input().strip()
print(*final_positions(S))

# """ This is the one that works but why??? """
# r = [i+(j=="R"or-1)for i,j in enumerate(input())]
# for i in range(30):
#      r = [r[i]for i in r]
# d = [0]*len(r)
# for i in r:
#      d[i]+=1
# print(*d)