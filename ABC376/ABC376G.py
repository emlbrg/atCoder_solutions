"""
G - Treasure Hunting
url: https://atcoder.jp/contests/abc376/tasks/abc376_g
"""
from operator import lt

class PriorityQueue:
    def __init__(self, compare_func=lt):
        self.heap = []
        self.compare_func = compare_func

    def push(self, item):
        # append item to the heap and adjust upwards
        self.heap.append(item)
        self._adjust_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("pop from an empty priority queue")

        # swap the root with the last item, pop it, and adjust downwards
        self._swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        self._adjust_down(0)
        return item

    def peek(self):
        if not self.heap:
            raise IndexError("peek from an empty priority queue")
        return self.heap[0]

    def _adjust_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.compare_func(self.heap[index], self.heap[parent]):
                self._swap(index, parent)
                index = parent
            else:
                break

    def _adjust_down(self, index):
        n = len(self.heap)
        while 2 * index + 1 < n:
            smallest = 2 * index + 1
            if smallest + 1 < n and self.compare_func(self.heap[smallest + 1], self.heap[smallest]):
                smallest += 1
            if self.compare_func(self.heap[smallest], self.heap[index]):
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __len__(self):
        return len(self.heap)


class UnionFind:
    def __init__(self, size):
        self.parent = [-1] * size

    def find_root(self, x):
        if self.parent[x] < 0:  # path compression for faster access
            return x
        self.parent[x] = self.find_root(self.parent[x])
        return self.parent[x]

    def are_connected(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def unite(self, x, y):
        # here `x` is the new root of the union by default...?
        root_x = self.find_root(x)
        root_y = self.find_root(y)
        if root_x != root_y:
            self.parent[root_x] += self.parent[root_y]
            self.parent[root_y] = root_x
            return True
        return False

    def size(self, x):
        return -self.parent[self.find_root(x)]


def solve(n, connections, values):
    MOD = 998244353
    total_sum = sum(values)
    result = 0
    union_find = UnionFind(n + 1)

    def priority_cmp(item1, item2):
        return item1[0] * item2[1] > item1[1] * item2[0]

    priority_queue = PriorityQueue(priority_cmp)
    sums = [0] * (n + 1)
    counts = [1] * (n + 1)

    for index, value in enumerate(values, start=1):
        priority_queue.push((value, 1, index))
        sums[index] = value

    for _ in range(n):
        while True:
            a, b, index = priority_queue.pop()
            if sums[index] == a and counts[index] == b:
                break

        root = union_find.find_root(connections[index - 1])
        result += counts[root] * a
        result %= MOD
        sums[root] += a
        counts[root] += b
        union_find.unite(root, index)
        
        if root != 0:
            priority_queue.push((sums[root], counts[root], root))

    result *= pow(total_sum, -1, MOD)
    result %= MOD

    return result


t = int(input())
for _ in range(t):
    n = int(input())
    connections = list(map(int, input().split()))
    values = list(map(int, input().split()))
    print(solve(n, connections, values))
