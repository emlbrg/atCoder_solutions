import numpy as np
from scipy.optimize import linear_sum_assignment

def do_the_thing():
    num_points = int(input())
    points_A = [list(map(int, input().split())) for _ in range(num_points)]
    points_B = [list(map(int, input().split())) for _ in range(num_points)]

    distance_matrix = np.zeros((num_points, num_points))
    
    for i in range(num_points):
        x_a, y_a = points_A[i]
        for j in range(num_points):
            x_b, y_b = points_B[j]
            distance_matrix[i][j] = np.sqrt((x_a - x_b) ** 2 + (y_a - y_b) ** 2)

    row_indices, col_indices = linear_sum_assignment(distance_matrix)

    print(*[index + 1 for index in col_indices])

do_the_thing()