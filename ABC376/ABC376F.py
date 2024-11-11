"""
F - Hands on Ring (Hard)
url: https://atcoder.jp/contests/abc376/tasks/abc376_f
"""
n, q = map(int, input().split())

# Initialize the `dp` array with a massive "impossible" value for all but the first position.
# The idea here: start on level zero, everywhere else is a nightmare.
dp = [0] + [10**9] * (n - 1)

# Set initial values for `g` (the direction) and `lr` (last recorded position).
g = 'R'
lr = 1

# go through each query and think of `eq` as our new "potential dp" for this round.
for _ in range(q):
    h, t = input().split()
    t = int(t) - 1

    # new array of "impossible" values because we love fresh starts.
    eq = [10**9] * n

    if g == h:
        # The gods of randomness favor us: we move in the same direction.
        for i, v in enumerate(dp):
            if lr == t:
                # If we're already at `t`, no need to move. Just chill.
                eq[i] = min(eq[i], v)
            elif i == t:
                # Time to play hopscotch around `t`!
                j = (t - 1) % n
                eq[j] = min(eq[j], v + 1 + (lr + n - t) % n)
                
                j = (t + 1) % n
                eq[j] = min(eq[j], v + 1 + (t + n - lr) % n)
            elif t <= lr <= i or i <= t <= lr or lr <= i <= t:
                # We're somewhere between `lr`, `i`, and `t`—let’s pick the least exhausting path
                j = (t + 1) % n
                eq[j] = min(eq[j], v + (j + n - i) % n + (t + n - lr) % n)
                
                j = i
                eq[j] = min(eq[j], v + (lr + n - t) % n)
            else:
                # Absolute chaos. Time to try every option with a convoluted calculation.
                j = (t - 1) % n
                eq[j] = min(eq[j], v + (i + n - j) % n + (lr + n - t) % n)
                
                j = i
                eq[j] = min(eq[j], v + (t + n - lr) % n)
    else:
        # Change of direction, new challenges.
        for i, v in enumerate(dp):
            if i == t:
                # A rare moment of rest for `lr`
                eq[lr] = min(eq[lr], v)
            elif lr == t:
                # Time to make the rounds from `t` again
                j = (t + 1) % n
                eq[j] = min(eq[j], v + 1 + (t + n - i) % n)
                
                j = (t - 1) % n
                eq[j] = min(eq[j], v + 1 + (i + n - t) % n)
            elif t <= lr <= i or i <= t <= lr or lr <= i <= t:
                # Just barely within bounds—try all the dance moves
                j = (t - 1) % n
                eq[j] = min(eq[j], v + (lr + n - j) % n + (i + n - t) % n)
                
                j = lr
                eq[j] = min(eq[j], v + (t + n - i) % n)
            else:
                # Utter mayhem: default to the crazy calculations.
                j = (t + 1) % n
                eq[j] = min(eq[j], v + (j + n - lr) % n + (t + n - i) % n)
                
                j = lr
                eq[j] = min(eq[j], v + (i + n - t) % n)
    
    dp = eq  # uptade dp = eq for this round
    g = h  # update direction
    lr = t  # and position

# least exhausting path result tho I am exhausted
print(min(dp))
