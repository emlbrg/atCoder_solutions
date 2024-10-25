"""
B - Interactive Sorting
url: https://atcoder.jp/contests/practice/tasks/practice_2

Problem Statement (my explanation)

You have to compare the weights of balls and sort them in ascending order using the minimal
number of queries possible. The balls are labeled with the first N uppercase letters, and
the goal is to output their sorted order based on their weights. 

You can compare two balls at a time using at most Q queries.

Input:
The number of balls N (up to 26).
The number of allowed queries Q.

You can query the system to compare the weight of two distinct balls in the form:
? A B
Where A and B are distinct letters representing the balls.

Output:
The system will respond with either > or <, indicating which of the two balls is heavier.
After sorting the balls, output the sorted order in the form:
! ABCDE... (the sorted ascending order)
"""
from string import ascii_uppercase
from typing import List

def compare(a: str, b: str) -> str:
    """
    Compare two balls a and b by querying the system.
    
    Args:
        a (str): The label of the first ball.
        b (str): The label of the second ball.
    
    Returns:
        str: The result of the comparison, either '>' if a is heavier than b, or '<' if b is heavier than a.
    """
    print(f"? {a} {b}", flush=True)
    return input()

def sort5(balls: List[str]) -> List[str]:
    """
    Sort exactly 5 balls using pairwise comparisons.
    
    Args:
        balls (List[str]): A list of 5 ball labels to be sorted.
    
    Returns:
        List[str]: A list of sorted ball labels.
    """
    a, b, c, d, e = balls

    # Pairwise comparisons and swaps to partially order the balls
    if compare(a, b) == ">": a, b = b, a  # noqa: E701
    if compare(c, d) == ">": c, d = d, c  # noqa: E701
    if compare(a, c) == ">": a, b, c, d = c, d, a, b  # noqa: E701

    if compare(c, e) == "<":
        if compare(d, e) == ">": d, e = e, d  # noqa: E701
        if compare(b, d) == "<":
            if compare(b, c) == "<":
                return [a, b, c, d, e]
            return [a, c, b, d, e]
        if compare(b, e) == "<":
            return [a, c, d, b, e]
        return [a, c, d, e, b]
    if compare(a, e) == "<":
        if compare(b, c) == "<":
            if compare(b, e) == "<":
                return [a, b, e, c, d]
            return [a, e, b, c, d]
        if compare(b, d) == "<":
            return [a, e, c, b, d]
        return [a, e, c, d, b]
    if compare(b, c) == "<":
        return [e, a, b, c, d]
    if compare(b, d) == "<":
        return [e, a, c, b, d]
    return [e, a, c, d, b]


def merge_sort(balls: List[str]) -> List[str]:
    """
    Recursive merge sort function for sorting the balls interactively.
    
    Args:
        balls (List[str]): A list of ball labels to be sorted.
    
    Returns:
        List[str]: A sorted list of ball labels.
    """
    if len(balls) <= 1:
        return balls

    mid = len(balls) // 2
    left = merge_sort(balls[:mid])
    right = merge_sort(balls[mid:])

    return merge(left, right)


def merge(left: List[str], right: List[str]) -> List[str]:
    """
    Merge two sorted halves interactively by querying comparisons.
    
    Args:
        left (List[str]): The sorted left half of ball labels.
        right (List[str]): The sorted right half of ball labels.
    
    Returns:
        List[str]: A merged and sorted list of ball labels.
    """
    merged = []
    l_i, r_i = 0, 0

    while l_i < len(left) and r_i < len(right):
        if compare(left[l_i], right[r_i]) == "<":
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    merged.extend(left[l_i:])
    merged.extend(right[r_i:])
    return merged


def main() -> None:
    """
    Main function to handle input, sorting, and output of the sorted order of balls.
    """
    n, q = map(int, input().split())
    balls = list(ascii_uppercase[:n])

    # Use a specialized sort for exactly 5 balls, otherwise use merge sort
    sorted_balls = sort5(balls) if n == 5 else merge_sort(balls)

    print(f"! {''.join(sorted_balls)}", flush=True)


if __name__ == "__main__":
    main()
