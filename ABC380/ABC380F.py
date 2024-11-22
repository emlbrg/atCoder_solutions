"""F - Exchange Game
url: https://atcoder.jp/contests/abc380/tasks/abc380_f
"""
# Added lots of comments becasue otherwise I will never be able to rember the heck I did
import sys

input = sys.stdin.readline

num_A, num_B, num_C = map(int, input().split())  # Sizes of groups A, B, and C
group_A = list(map(int, input().split()))        # Values in group A
group_B = list(map(int, input().split()))        # Values in group B
group_C = list(map(int, input().split()))        # Values in group C

# Combine all groups into a single list
combined_values = group_A + group_B + group_C
total_elements = len(combined_values)

# Cache for memoization to store game states
# 1: Takahashi wins, 0: Aoki wins, -1: undecided
game_state_cache = [-1] * (1 << 24)  # Supports up to 24 elements (2^24 states)

def can_takahashi_win(first_player: int, second_player: int) -> int:
    """
    Determines if Takahashi can force a win given the current state.
    Args:
    - first_player: bitmask representing elements controlled by the first player (Takahashi).
    - second_player: bitmask representing elements controlled by the second player (Aoki).

    Returns:
    - 1 if Takahashi can guarantee a win.
    - 0 if Aoki can prevent Takahashi from winning.
    """
    state_key = (first_player << 12) | second_player  # use a single integer to represent the state in the cache
    if game_state_cache[state_key] != -1:
        return game_state_cache[state_key]

    current_positions = []  # lists of current positions and possible moves
    possible_moves = []

    for i in range(total_elements):
        if first_player & (1 << i):  # Element controlled by Takahashi
            current_positions.append(i)
        elif not second_player & (1 << i):  # Element not controlled by Aoki
            possible_moves.append(i)

    # Try all moves from current positions
    for current in current_positions:
        # Takahashi moves this element
        next_first = first_player ^ (1 << current)  # Remove the element from Takahashi's control
        if not can_takahashi_win(second_player, next_first):  # Switch roles
            game_state_cache[state_key] = 1
            return 1

        # Try swapping the current element with any eligible element
        for target in possible_moves:
            if combined_values[target] < combined_values[current]:  # Only swap if target is smaller
                next_first = first_player ^ (1 << current) ^ (1 << target)
                if not can_takahashi_win(second_player, next_first):  # Switch roles
                    game_state_cache[state_key] = 1
                    return 1

    # If no winning move is found, Aoki can prevent Takahashi's win
    game_state_cache[state_key] = 0
    return 0

# Initialize starting states for Takahashi and Aoki
takahashi_state = 0
aoki_state = 0

# Set initial elements controlled by Takahashi
for i in range(num_A):
    takahashi_state |= 1 << i

# Set initial elements controlled by Aoki
for i in range(num_B):
    aoki_state |= 1 << (i + num_A)

winner = "Takahashi" if can_takahashi_win(takahashi_state, aoki_state) else "Aoki"
print(winner)
