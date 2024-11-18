"""
D - Strange Mirroring
url: https://atcoder.jp/contests/abc380/tasks/abc380_d
"""
import sys

input = sys.stdin.readline
string = input().strip()
num_queries = int(input())
queries = list(map(int, input().split()))


def get_character_at_index(index):
    """
    Determines the character at a given index in the expanded string.
    The expansion doubles the string length, with an inversion for the second half.
    """
    is_inverted = False
    original_length = len(string)
    expanded_length = original_length

    while expanded_length < index:
        expanded_length *= 2

    while expanded_length > original_length:
        mid_point = expanded_length // 2
        if index > mid_point:
            index -= mid_point
            is_inverted = not is_inverted
        expanded_length = mid_point

    char = string[index - 1]
    if is_inverted:
        char = char.swapcase()

    return char


result = [get_character_at_index(k) for k in queries]
print(" ".join(result))
