"""
A - Irreversible operation
url: https://atcoder.jp/contests/agc029/tasks/agc029_a

The problem involves manipulating a string representing Reversi pieces, 
where each piece can either be black ('B') or white ('W').

You can perform a specific operation where you flip adjacent pieces 
that have a BLACK PIECE ON THE LEFT and a WHITE PIECE ON THE RIGHT. 
Your goal is to determine how many times you can perform this operation until no more valid flips can be made.

Example:
For the input BBW:

Initial state: B B W
Valid pairs for operation:
(Index 2 and 3): Flip B at index 2 and W at index 3 → Resulting string: B W B
(Index 1 and 2): Now you can flip B at index 1 and W at index 2 → Resulting string: W B B
After these two operations, no further 'BW' pairs can be formed. Hence, the maximum number of operations is 2.
"""
def max_flips(S: str):
    count = 0
    while True:
        found = False
        for i in range(len(S) - 1):
            if S[i] == 'B' and S[i + 1] == 'W':
                S = S[:i] + 'W' + 'B' + S[i + 2:]
                count += 1
                found = True
                break
        if not found:
            break
    return count

S = input().strip()
print(max_flips(S))


""" Faster implementation in case of TLE """
# def max_flips(S: str) -> int:
#     count_B = 0  # Count of consecutive 'B's
#     flips = 0     # Total number of flips

#     # Iterate through the string
#     for char in S:
#         if char == 'B':
#             count_B += 1  # Increment count of 'B's
#         elif char == 'W':
#             flips += count_B  # Each 'B' can flip with this 'W'

#     return flips

# S = input().strip()
# print(max_flips(S))
