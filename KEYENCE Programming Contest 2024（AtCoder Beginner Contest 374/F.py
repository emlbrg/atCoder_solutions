"""
F - Shipping
url: https://atcoder.jp/contests/abc374/tasks/abc374_f

"""
from collections import defaultdict
from typing import List

def minimum_dissatisfaction(n: int, k: int, x: int, t: List[int]) -> int:
    """
    Calculates the minimum dissatisfaction given a sequence of tasks over specified time intervals.

    Args:
        n (int): Total number of tasks.
        k (int): Maximum number of consecutive tasks that can be grouped.
        x (int): Interval offset.
        t (List[int]): List of task dissatisfaction values.

    Returns:
        int: Minimum dissatisfaction possible for the given configuration.
    """
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + t[i]

    dp = [defaultdict(lambda: float('inf')) for _ in range(n + 1)]
    dp[0][-x] = 0  # Base case: zero dissatisfaction with initial offset day -x


    for i in range(n):
        sorted_entries = sorted(dp[i].items())
        min_cost = float('inf')
        pruned_dp_i = {}
        for day, cost in sorted_entries:
            if cost < min_cost:
                min_cost = cost
                pruned_dp_i[day] = cost
        dp[i] = pruned_dp_i

        for start_day in dp[i]:
            base_cost = dp[i][start_day]
            max_task_dissatisfaction = t[i]
            for group_size in range(1, k + 1):
                end_idx = i + group_size
                if end_idx > n:
                    break

                max_task_dissatisfaction = max(max_task_dissatisfaction, t[end_idx - 1])
                next_start_day = max(start_day + x, max_task_dissatisfaction)
                total_dissatisfaction = group_size * next_start_day - (prefix_sum[end_idx] - prefix_sum[i])

                new_cost = base_cost + total_dissatisfaction
                if dp[end_idx][next_start_day] > new_cost:
                    dp[end_idx][next_start_day] = new_cost

    return int(min(dp[n].values()))

n, k, x = map(int, input().split())
t = list(map(int, input().split()))
print(minimum_dissatisfaction(n, k, x, t))

