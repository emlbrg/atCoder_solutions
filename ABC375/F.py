import sys
import numpy as np

def main():

    def input():  # I can't believe this works like this
        return sys.stdin.readline()
    
    N, M, Q = map(int, sys.stdin.readline().split())
    roads = [None]  # roads[1..M]
    for _ in range(M):
        A, B, C = map(int, sys.stdin.readline().split())
        roads.append((A, B, C))
    
    queries = []
    closed_roads = set()
    for _ in range(Q):
        tmp = sys.stdin.readline().split()
        if tmp[0] == '1':
            i = int(tmp[1])
            queries.append(('close', i))
            closed_roads.add(i)
        else:
            x, y = int(tmp[1]), int(tmp[2])
            queries.append(('query', x, y))
    
    # Initialize distance matrix with INF
    INF = float('inf')
    dist = np.full((N+1, N+1), INF, dtype=np.float64)
    np.fill_diagonal(dist, 0)
    
    # Add roads that are not closed by any close query
    for i in range(1, M+1):
        if i not in closed_roads:
            A, B, C = roads[i]
            if dist[A][B] > C:
                dist[A][B] = C
                dist[B][A] = C
    
    # Initial Floyd-Warshall
    for k in range(1, N+1):
        # Broadcasting: dist[:, k] + dist[k, :] 
        # We need to avoid overflow by setting where dist[:, k] == INF or dist[k, :] == INF
        dist_k = dist[:, k].reshape((N+1, 1))
        dist_k_plus = dist[k, :].reshape((1, N+1))
        new_dist = dist_k + dist_k_plus
        dist = np.minimum(dist, new_dist)
    
    # Prepare to process queries in reverse
    answers = []

    # Process queries in reverse
    for q in reversed(queries):
        if q[0] == 'query':
            x, y = q[1], q[2]
            distance = dist[x][y]
            if distance == INF:
                answers.append(-1)
            else:
                # Convert to integer if needed
                answers.append(int(distance))
        else:
            # 'close' in original is 'add' in reverse
            i = q[1]
            A, B, C = roads[i]
            # If the road was already closed, add it back
            # Update distance matrix with the new road
            # Only update if this road provides a shorter path
            # Update dist[A][B] and dist[B][A]
            if dist[A][B] > C:
                dist[A][B] = C
                dist[B][A] = C
            # Now, perform Floyd-Warshall updates for the added road
            # Update dist[i][j] = min(dist[i][j], dist[i][A] + C + dist[B][j], dist[i][B] + C + dist[A][j])
            # Using Numpy for vectorized operations
            # Update via A
            dist = np.minimum(dist, dist[:, A].reshape(N+1,1) + C + dist[B, :].reshape(1, N+1))
            # Update via B
            dist = np.minimum(dist, dist[:, B].reshape(N+1,1) + C + dist[A, :].reshape(1, N+1))
    
    # Reverse the answers to original order
    for ans in reversed(answers):
        print(ans)

if __name__ == "__main__":
    main()