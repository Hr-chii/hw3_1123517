# hw3_1123517 Callie
##Question: 1
Given an undirected graph with V nodes and E edges, create and return an adjacency list of the graph. 0-based indexing is followed everywhere.
Examples: (Should not use the examples to submit your code. These examples are for your understanding)
Input:
V = 6
edges = [[0, 2], [0, 5], [5, 2], [4, 3], [2, 3], [3, 1], [4, 1]]

Output: 
[[2, 5], [3, 4], [0, 5, 3], [4, 2, 1], [3, 1], [0, 2]]

##Question: 2
Given a connected undirected graph represented by an adjacency list adj, which is a vector of vectors where each adj[i] represents the list of vertices connected to vertex i. Perform a Breadth First Traversal (BFS) starting from vertex 0, visiting vertices from left to right according to the adjacency list, and return a list containing the BFS traversal of the graph.
Note: Do traverse in the same order as they are in the adjacency list.
Examples: (Should not use the examples to submit your code. These examples are for your understanding)
Input:
[[1, 4, 5], [0, 2], [1, 3], [2, 4], [0, 3], [0]]

Output:
[0, 1, 4, 5, 2, 3]

##Question: 3
Given a connected undirected graph represented by an adjacency list adj, which is a vector of vectors where each adj[i] represents the list of vertices connected to vertex i. Perform a Depth First Traversal (DFS) starting from vertex 0, visiting vertices from left to right as per the adjacency list, and return a list containing the DFS traversal of the graph.
Note: Do traverse in the same order as they are in the adjacency list.
Examples: (Should not use the examples to submit your code. These examples are for your understanding)
Input: adj =[[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3], [2]]

Output: 
[0, 1, 2, 5, 4, 3]

##Question: 4
Given a weighted, undirected, and connected graph with V vertices and E edges, your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. The graph is represented by an adjacency list, where each element adj[i] is a vector containing vector of integers. Each vector represents an edge, with the first integer denoting the endpoint of the edge and the second integer denoting the weight of the edge.
Examples: (Should not use the examples to submit your code. These examples are for your understanding)
Input:
V = 4
edges = [(0, 1, 2), (1, 3, 6), (0, 2, 3), (2, 3, 1)]

Output:
6


