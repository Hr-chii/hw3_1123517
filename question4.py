#Callie
#1123517
#2024/12/12

import heapq

def mst_weight_sum(V, edges):
    adj = [[] for _ in range(V)]
    for u, v, weight in edges:
        adj[u].append((weight, v))
        adj[v].append((weight, u))

    visited = [False] * V
    min_heap = [(0, 0)] 
    mst_sum = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        mst_sum += weight
        for next_weight, neighbor in adj[node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (next_weight, neighbor))

    return mst_sum

V = 4
edges = [(0, 1, 2), (1, 3, 6), (0, 2, 3), (2, 3, 1)]
print(mst_weight_sum(V, edges))

# Example usage
#V = 3
#edges = [(0, 1, 5), (1, 2, 3), (0, 2, 1)]
#print(mst_weight_sum(V, edges))