"""
F - Knapsack with Diminishing Values
url: https://atcoder.jp/contests/abc373/tasks/abc373_f
"""
from collections import defaultdict
from pulp import (
    LpBinary,
    LpMaximize,
    LpProblem,
    LpVariable,
    PULP_CBC_CMD,
    lpDot,
    value,
)

N, WW = map(int, input().split())
W, V = [], []
X = []
for i in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
    
prob = LpProblem(name='ABC373_F', sense=LpMaximize)
obj = 0
const = 0
D = defaultdict(list)
for i in range(N):
    w, v = W[i], V[i]
    m = WW // w + 1    
    for j in range(m):
        D[w].append(v - (2 * j + 1)) 

W2, V2 = [], []
cnt = 0
for i in range(1, 3005):
    if not D[i]:
        continue
    L = D[i]
    L.sort(reverse=True)
    m = WW // i + 1
    while len(L) >= m:
        L.pop()
    for v in L:
        W2.append(i)
        V2.append(v)
        X.append(LpVariable(name=str(cnt), cat=LpBinary))
        cnt += 1
    
prob += lpDot(V2, X)
prob += lpDot(W2, X) <= WW
status = prob.solve(PULP_CBC_CMD(msg = False, timeLimit=2))
print(int(value(prob.objective)))
