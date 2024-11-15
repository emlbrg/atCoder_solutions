"""
D - Buildings
url: https://atcoder.jp/contests/abc372/tasks/abc372_d
"""
N = int(input())
H = list(map(int, input().split(" ")))

res = [0]*N
stk = []
for i in range(N-2, -1, -1):  #i+1 <= N-1
  while stk and H[stk[-1]] < H[i+1]:
    stk.pop()

  stk.append(i+1)
  res[i] = len(stk)
  
print(*res)