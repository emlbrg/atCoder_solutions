"""
url: https://atcoder.jp/contests/arc185/tasks/arc185_b
"""
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    total_sum = sum(a)

    base_value = total_sum // n
    remainder = total_sum % n

    b = [base_value] * (n - remainder) + [base_value + 1] * remainder

    is_possible = True
    for i in range(n - 1):
        if a[i] > b[i]:
            is_possible = False
            break
        
        a[i + 1] -= (b[i] - a[i])

    print("Yes" if is_possible else "No")



