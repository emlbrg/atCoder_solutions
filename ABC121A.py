"""
A - White Cells
url: https://atcoder.jp/contests/abc121/tasks/abc121_a
"""

def remaining_white_cells(H, W, h, w):
    total_cells = H * W
    painted_cells = (h * W) + (w * H) - (h * w)
    remaining_cells = total_cells - painted_cells
    return remaining_cells

H, W = map(int, input().split())
h, w = map(int, input().split())

print(remaining_white_cells(H, W, h, w))
