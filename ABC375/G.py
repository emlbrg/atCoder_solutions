from heapq import heappop, heappush
import sys

sys.setrecursionlimit(1000000)

INF = int(1e18)

def dijkstra(start, graph, num_nodes):
    """Perform Dijkstra's algorithm to find the shortest paths from the start node."""
    dist = [INF] * num_nodes
    dist[start] = 0
    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heappop(priority_queue)
        
        if current_distance > dist[current_node]:
            continue

        for neighbor, _, cost in graph[current_node]:
            new_distance = current_distance + cost
            if new_distance < dist[neighbor]:
                dist[neighbor] = new_distance
                heappush(priority_queue, (new_distance, neighbor))

    return dist

def find_shortest_edges(edges, dist_from_start, dist_from_end, target_distance):
    """Determine which edges are part of any shortest path."""
    shortest_edges = []
    for A, B, C in edges:
        # check both paths: 0 -> A -> B -> (N-1) and 0 -> B -> A -> (N-1)
        path_length = dist_from_start[A] + C + dist_from_end[B]
        path_length = min(path_length, dist_from_start[B] + C + dist_from_end[A])
        shortest_edges.append(path_length == target_distance)
    return shortest_edges

def dfs(node, parent, graph, ord, low, shortest_edges, last_ord):
    """Depth-First Search for bridge detection."""
    last_ord += 1
    ord[node] = last_ord
    low[node] = ord[node]

    for neighbor, edge_index, _ in graph[node]:
        if not shortest_edges[edge_index]: 
            continue
        if neighbor == parent: 
            continue

        if ord[neighbor] == INF:
            last_ord = dfs(neighbor, node, graph, ord, low, shortest_edges, last_ord)
            low[node] = min(low[node], low[neighbor])
        else:
            low[node] = min(low[node], ord[neighbor])

    return last_ord

def road_block():
    """Main function to determine road block bridges."""
    num_nodes, num_edges = map(int, input().split())
    graph = [[] for _ in range(num_nodes)]
    edges = []

    for edge_index in range(num_edges):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        edges.append((A, B, C))

        graph[A].append((B, edge_index, C))
        graph[B].append((A, edge_index, C))

    dist_from_start = dijkstra(0, graph, num_nodes)
    dist_from_end = dijkstra(num_nodes - 1, graph, num_nodes)

    target_distance = dist_from_start[num_nodes - 1]
    shortest_edges = find_shortest_edges(edges, dist_from_start, dist_from_end, target_distance)

    ord = [INF] * num_nodes
    low = [INF] * num_nodes
    last_ord = 0

    dfs(0, -1, graph, ord, low, shortest_edges, last_ord)

    results = []
    for edge_index in range(num_edges):
        A, B, _ = edges[edge_index]
        is_bridge = shortest_edges[edge_index] and (ord[A] < low[B] or ord[B] < low[A])
        results.append("Yes" if is_bridge else "No")

    print("\n".join(results))

road_block()

