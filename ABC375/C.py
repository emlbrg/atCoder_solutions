N = int(input())
grid = [list(input().strip()) for _ in range(N)]

for layer in range(0, N // 2):
    for cell in range(layer, N - layer - 1):
        increment = layer + 1
        temp = [grid[layer][cell],
        grid[cell][N - 1 - layer],
        grid[N - 1 - layer][N - 1 - cell],
        grid[N - 1 - cell][layer]]

        grid[layer][cell] = temp[(0 - increment % 4)]
        grid[cell][N - 1 - layer] = temp[(1 - increment % 4)]
        grid[N - 1 - layer][N - 1 - cell] = temp[(2 - increment % 4)]
        grid[N - 1 - cell][layer] = temp[(3 - increment % 4)]

for row in grid:
    print(''.join(row))