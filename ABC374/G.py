"""
G - Only One Product Name
url: https://atcoder.jp/contests/abc374/tasks/abc374_g

Problem Statement
All KEYENCE product names consist of two uppercase English letters.
They have already used N product names, the i-th of which (1≤i≤N) is Si.
Once a product name is used, it cannot be reused, so they decided to create an NG (Not Good) list to quickly identify previously used product names.

The NG list must satisfy the following conditions.

It consists of one or more strings, each consisting of uppercase English letters.
For each already used product name, there exists at least one string in the list that contains the name as a (contiguous) substring.
None of the strings in the list contain any length-2 (contiguous) substring that is not an already used product name.
Find the minimum possible number of strings in the NG list.

Input (the NG list)
The input is given from Standard Input in the following format:
N (no. of prodict names)
S1
S2
⋮
SN

Output
Print the minimum possible number of strings in the NG list.
"""
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix  # type: ignore
from scipy.sparse.csgraph import connected_components, floyd_warshall, maximum_bipartite_matching  # type: ignore

N = int(input())
products = []

for _ in range(N):
    S = input()
    products.append(S)

def find_scc(n: int, products: list[str]) -> tuple[int, np.ndarray, list[list[int]]]:
    """
    Find strongly connected components (SCCs) in a directed graph of products.
    
    Args:
        n (int): The number of products.
        products (list[str]): A list of product strings.
    
    Returns:
        tuple[int, np.ndarray, list[list[int]]]: A tuple containing the number of SCCs, 
            the labels of each product indicating which SCC they belong to, 
            and the adjacency matrix of the graph.
    """
    product_index = {product: i for i, product in enumerate(products)}
    
    graph = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if products[i][1] == products[j][0] and i != j:
                graph[product_index[products[i]]][product_index[products[j]]] = 1
    

    graph_csr = csr_matrix(graph)
    

    num_scc, labels = connected_components(graph_csr, connection='strong')
    
    return num_scc, labels, graph

num_scc, labels, graph = find_scc(N, products)


scc_graph = [[0] * num_scc for _ in range(num_scc)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            scc_from = labels[i]
            scc_to = labels[j]
            if scc_from != scc_to:
                scc_graph[scc_from][scc_to] = 1

scc_graph_csr = csr_matrix(scc_graph)
reachability_matrix = floyd_warshall(scc_graph_csr, directed=True)

scc_graph_edges = set()
for i in range(num_scc):
    for j in range(num_scc):
        if i != j and reachability_matrix[i, j] < float('inf'):
            scc_graph_edges.add((i, j))

bipartite_edges = [(u, v + num_scc) for u, v in scc_graph_edges]

if len(bipartite_edges) != 0:
    i, j = list(zip(*bipartite_edges))
    ones = np.ones(len(bipartite_edges), dtype=np.int64).T
    coo = coo_matrix((ones, (i, j)), (2 * num_scc, 2 * num_scc))

    matching = maximum_bipartite_matching(coo)
    max_matching_size = np.count_nonzero(matching != -1)
else:
    max_matching_size = 0

min_path_cover_size = num_scc - max_matching_size

print(min_path_cover_size)
