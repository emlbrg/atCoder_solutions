"""
D - Laser Marking
url: https://atcoder.jp/contests/abc374/tasks/abc374_d

There is a printing machine that prints line segments on the xy-plane by emitting a laser.

At the start of printing, the laser position is at coordinate (0,0).
When printing a line segment, the procedure below is followed.

First, move the laser position to one of the endpoints of the line segment.
One may start drawing from either endpoint.
Then, move the laser position in a straight line from the current endpoint to the other endpoint while emitting the laser.
It is not allowed to stop printing in the middle of a line segment.
When not emitting the laser, the laser position can move in any direction at a speed of S units per second.

When emitting the laser, the laser position can move along the line segment being printed at a speed of T units per second.
The time required for operations other than moving the laser position can be ignored.
Takahashi wants to print N line segments using this printing machine.
The i-th line segment connects coordinates (Ai, Bi) and (Ci ,Di).
Some line segments may overlap, in which case he needs to print the overlapping parts for each line segment separately.

What is the minimum number of seconds required to complete printing all the line segments when he operates the printing machine optimally?

TL/DR:
This code solves a combinatorial problem where you need to print line segments on an xy-plane using a laser printer that can move freely when the laser is off and at a reduced speed when the laser is on.
"""

import itertools
import math

def calculate_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points (x1, y1) and (x2, y2)."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_min_time(n: int, S: int, T: int, segments: list) -> float:
    """
    Calculate the minimum time to print all line segments optimally.

    Args:
        n (int): Number of line segments.
        S (int): Speed when moving without laser.
        T (int): Speed when moving with laser.
        segments (list[tuple]): List of segments as tuples (Ax, Ay, Bx, By).

    Returns:
        float: Minimum time required to print all line segments.
    """
    # Create all possible start-end configurations for each segment
    possible_orientations = []
    for (Ax, Ay, Bx, By) in segments:
        possible_orientations.append([((Ax, Ay), (Bx, By)), ((Bx, By), (Ax, Ay))])

    min_time = float('inf')
    # Iterate over all possible combinations of start-end orientations
    for orientation in range(2 ** n):
        # Select one orientation for each segment
        selected_segments = [possible_orientations[i][(orientation >> i) & 1] for i in range(n)]
        # Check all orderings of the selected orientations
        for segment_order in itertools.permutations(selected_segments):
            time = 0
            previous_position = (0, 0)  # Start at the origin
            # Calculate time for this specific ordering
            for (start, end) in segment_order:
                time += calculate_distance(*previous_position, *start) / S  # Move to start point
                time += calculate_distance(*start, *end) / T               # Print line segment
                previous_position = end
            min_time = min(min_time, time)

    return min_time

# Input parsing
n, S, T = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Output the minimum time required
print(calculate_min_time(n, S, T, segments))
