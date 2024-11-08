"""
C - Prepare Another Box
ur: https://atcoder.jp/contests/abc376/tasks/abc376_c
"""
def can_place_all_toys(N, toys, boxes, x):
    # Sort toys and the available boxes including new box of size x
    toys.sort()
    all_boxes = boxes + [x]
    all_boxes.sort()
    
    # Try to match each toy to a box
    i, j = 0, 0  # pointers for toys and boxes
    while i < N and j < N:
        if all_boxes[j] >= toys[i]:  # current box can fit current toy
            i += 1  # move to the next toy
        j += 1  # move to the next box
    return i == N  # return True if all toys are placed

def find_min_x(N, toys, boxes):
    left, right = 1, max(max(toys), max(boxes))  # binary search range
    answer = -1  # default to -1 if no valid x is found

    while left <= right:
        mid = (left + right) // 2
        if can_place_all_toys(N, toys, boxes, mid):
            answer = mid  # mid is a valid x, try to find smaller
            right = mid - 1
        else:
            left = mid + 1  # increase x since mid is not sufficient
    
    return answer

# Input reading
N = int(input().strip())
toys = list(map(int, input().strip().split()))
boxes = list(map(int, input().strip().split()))

# Output result
print(find_min_x(N, toys, boxes))
