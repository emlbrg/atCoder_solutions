"""
url: https://atcoder.jp/contests/abc377/tasks/abc377_e
"""
import sys
input = sys.stdin.readline

word_count = int(input().strip())
results = []

# Trie structure initialization
next_nodes = [[-1] * 26]  # Each node has links to 26 possible children ("a" to "z")
parent_node = [-1]        # Tracks the parent node for each node
node_depth = [0]          # Tracks depth for each node in the trie
node_count = [0]          # Count for each node's occurrence
min_distance = [1 << 63]  # Initialize minimum distance for each node

total_nodes = 1  # Total number of nodes, starting with the root

for _ in range(word_count):
    word = input().strip()
    length = len(word)
    path = []

    current_node = 0
    for char in word:
        char_index = ord(char) - ord('a')
        
        # Add a new node if no link exists for the current character
        if next_nodes[current_node][char_index] == -1:
            next_nodes[current_node][char_index] = total_nodes
            next_nodes.append([-1] * 26)
            parent_node.append(current_node)
            node_depth.append(node_depth[current_node] + 1)
            node_count.append(0)
            min_distance.append(1 << 63)
            
            current_node = total_nodes
            total_nodes += 1
        else:
            # Move to the next node in the trie
            current_node = next_nodes[current_node][char_index]

        # Track the path of nodes visited
        path.append(current_node)

    node_count[current_node] += 1

    min_val = length  # minimum distances
    temp_min = 1 << 63
    position = 1

    for node in path:
        temp_min = min(temp_min, min_distance[node] + length - position)
        position += 1

    results.append(min(min_val, temp_min))

    # Update minimum distances for nodes in the path
    position = 1
    for node in path:
        min_distance[node] = min(min_distance[node], length - position)
        position += 1

# Output results for each word
print(*results)
