"""
E - Sensor Optimization Dilemma 2
url: https://atcoder.jp/contests/abc374/tasks/abc374_e
"""
from typing import List, Tuple

def judge(W: int, N: int, X: int, data: List[Tuple[int, int, int, int]]) -> bool:
    """
    Determine if it's possible to achieve a production capacity of W with the given budget.
    
    Args:
        W (int): Target production capacity per day.
        N (int): Number of processes.
        X (int): Total budget in yen.
        data (List[Tuple[int, int, int, int]]): Specifications for each process, 
            where each tuple contains (A, P, B, Q):
            A (int): Products per day by machine S.
            P (int): Cost per unit of machine S.
            B (int): Products per day by machine T.
            Q (int): Cost per unit of machine T.
    
    Returns:
        bool: True if the target capacity W is achievable within budget X, otherwise False.
    """
    total_cost = 0
    for A, P, B, Q in data:
        min_cost = float('inf')
        
        # Option 1: Using machine S primarily, limit to B units of S
        if A * Q < B * P:
            for j in range(B + 1):
                required_products = max(0, W - A * j)
                cost_s = P * j
                
                units_t = -(-required_products // B)  # Calculate the minimum units of T needed
                cost_total = cost_s + Q * units_t
                min_cost = min(min_cost, cost_total)
        else:
            # Option 2: Using machine T primarily, limit to A units of T
            for j in range(A + 1):
                required_products = max(0, W - B * j)
                cost_t = Q * j
                
                units_s = -(-required_products // A)  # Calculate the minimum units of S needed
                cost_total = cost_t + P * units_s
                min_cost = min(min_cost, cost_total)

        total_cost += min_cost
        if total_cost > X:
            return False
    
    return total_cost <= X

def max_production_capacity(N: int, X: int, data: List[Tuple[int, int, int, int]]) -> int:
    """
    Calculate the maximum achievable production capacity within the budget.
    
    Args:
        N (int): Number of processes.
        X (int): Total budget in yen.
        data (List[Tuple[int, int, int, int]]): List of machine specifications for each process.
    
    Returns:
        int: Maximum achievable production capacity.
    """
    ok, ng = -1, 10**12
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if judge(mid, N, X, data):
            ok = mid
        else:
            ng = mid
    return ok

N, X = map(int, input().split())
data = [tuple(map(int, input().split())) for _ in range(N)]

print(max_production_capacity(N, X, data))

### TESTING ###
# 10 7654321
# 8 6 9 1
# 5 6 4 3
# 2 4 7 9
# 7 8 9 1
# 7 9 1 6
# 4 8 9 1
# 2 2 8 9
# 1 6 2 6
# 4 2 3 4
# 6 6 5 2

