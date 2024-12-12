#Callie
#1123517
#2024/12/12

def dfs_traversal(adj):
    def dfs(node, visited, result):
        visited[node] = True
        result.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited, result)

    visited = [False] * len(adj)
    result = []
    dfs(0, visited, result)
    return result

adj_list = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3], [2]]
print(dfs_traversal(adj_list))

# Example usage
#adj_list = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
#print(dfs_traversal(adj_list))
