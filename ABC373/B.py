"""
B - 1D Keyboard
url: https://atcoder.jp/contests/abc373/tasks/abc373_b
"""
S = input().strip()

position = {char: idx + 1 for idx, char in enumerate(S)}

total_distance = 0

current_position = position['A']

for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    next_position = position[char]
    total_distance += abs(next_position - current_position)
    current_position = next_position

print(total_distance)

