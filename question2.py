#Callie
#1123517
#2024/12/12

def bfs_traversal(adj):
    visited = [False] * len(adj)
    queue = []
    traversal = []

    # 將起始節點 (0) 加入佇列並標記為已訪問
    queue.append(0)
    visited[0] = True

    while queue:
        node = queue.pop(0)
        traversal.append(node)
        
        for neighbor in adj[node]:
            # 如果鄰居還沒被訪問過，將它加入佇列並標記為已訪問
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return traversal

adj_list = [[1, 4, 5], [0, 2], [1, 3], [2, 4], [0, 3], [0]]
print(bfs_traversal(adj_list))

# Example usage
#nnn = [[2, 3, 1], [0], [0, 4], [0], [2]]
#print(bfs_traversal(nnn))
