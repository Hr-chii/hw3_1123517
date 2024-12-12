#Callie
#1123517
#2024/12/12

def create_adjacency_list(V, edges):
    adjacency_list = [[] for _ in range(V)]
    [[1], [0], [], []]
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    return adjacency_list

V = 6
edges = [[0, 2], [0, 5], [5, 2], [4, 3], [2, 3], [3, 1], [4, 1]]
print(create_adjacency_list(V, edges))


# Example usage
#V = 5
#edges = [[0, 1], [0, 4], [4, 1], [4, 3], [1, 3], [1, 2], [3, 2]]
#print(create_adjacency_list(V, edges))