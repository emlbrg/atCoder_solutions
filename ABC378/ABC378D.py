"""
D - Count Simple Paths
url: https://atcoder.jp/contests/abc378/tasks/abc378_d
"""
H, W, K = map(int, input().split())
grid = [input().strip() for _ in range(H)]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

valid_paths_count = 0

def dfs(x, y, steps, visited):
    global valid_paths_count
    if steps == K + 1:
        valid_paths_count += 1
        return

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and (nx, ny) not in visited and grid[nx][ny] == '.':
            visited.add((nx, ny))
            dfs(nx, ny, steps + 1, visited)
            visited.remove((nx, ny))

for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':
            dfs(i, j, 1, {(i, j)})

print(valid_paths_count)

