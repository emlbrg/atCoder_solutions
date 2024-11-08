"""
url: https://atcoder.jp/contests/abc368/tasks/abc368_f
"""
def prime_factors_count(n):
    factors = []
    num = n
    for i in range(2, int(n**0.5) + 1):
        if num % i == 0:
            count = 0
            while num % i == 0:
                count += 1
                num //= i
            factors.append((i, count))
    
    if num > 1:
        factors.append((num, 1))
    
    return sum(count for _, count in factors)

N = int(input())
A = list(map(int, input().split()))

factor_counts = [prime_factors_count(a) for a in A]

xor_sum = 0
for count in factor_counts:
    xor_sum ^= count

if xor_sum:
    print("Anna")
else:
    print("Bruno")


