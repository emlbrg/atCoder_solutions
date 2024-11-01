import math

def total_cost_of_journey():
    N = int(input())
    total_cost = 0.0
    
    current_x, current_y = 0, 0
    
    for _ in range(N):
        x, y = map(int, input().split())
        
        move_cost = math.sqrt((current_x - x) ** 2 + (current_y - y) ** 2)
        total_cost += move_cost
        
        current_x, current_y = x, y

    return_cost = math.sqrt(current_x ** 2 + current_y ** 2)
    total_cost += return_cost
    
    print(total_cost)

total_cost_of_journey()
