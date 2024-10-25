"""
B - Power Socket
url: https://atcoder.jp/contests/abc139/tasks/abc139_b

Problem Statement
Takahashi's house has only one socket.
Takahashi wants to extend it with some number of power strips, each with A sockets, into B or more empty sockets.
One power strip with A sockets can extend one empty socket into A empty sockets.

Find the minimum number of power strips required.

Constraints
All values in input are integers.
2≤A≤20
1≤B≤20

Input
Input is given from Standard Input in the following format:
A B

Output
Print the minimum number of power strips required.
"""
A, B = map(int, input().split())

# Story of my life!!! There are never enough sockets
sockets = 1
strips = 0

# While we don't have enough sockets
while sockets < B:
    # Add one power strip even tho it's a fire rosk
    strips += 1
    # Increase the number of sockets by A - 1...I wish
    sockets += A - 1

print(strips)


### TEST ###

# Input 1
#4 10

# Output 1
# 3
# 3 power strips, each with 4 sockets, extend the socket into 10 empty sockets.