import heapq

# Function to implement Prim's Algorithm
def prims_algorithm(graph, V):
    # Create a min heap to store the edges (weight, vertex)
    min_heap = [(0, 0)]  # (weight, vertex), starting from vertex 0
    visited = [False] * V  # Track visited vertices
    mst_cost = 0  # Total cost of the Minimum Spanning Tree
    mst_edges = []  # Store the edges of the MST

    while min_heap:
        # Pop the smallest edge from the heap
        weight, u = heapq.heappop(min_heap)
        
        if visited[u]:
            continue
        
        # Mark this vertex as visited
        visited[u] = True
        mst_cost += weight
        
        # Add this edge to the MST (only if it's not the initial dummy edge)
        if weight != 0:
            mst_edges.append((u, weight))
        
        # Go through all adjacent vertices of u
        for v, w in graph[u]:
            if not visited[v]:
                # Push the edge (weight, v) into the heap
                heapq.heappush(min_heap, (w, v))
    
    return mst_cost, mst_edges

# Driver code to test the function
if __name__ == "__main__":
    # Number of vertices
    V = 5
    
    # Graph represented as an adjacency list (vertex, weight)
    graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8)],
        4: [(1, 5), (2, 7)]
    }
    
    # Function call
    mst_cost, mst_edges = prims_algorithm(graph, V)
    
    print(f"Cost of Minimum Spanning Tree: {mst_cost}")
    print("Edges in the Minimum Spanning Tree:")
    for edge in mst_edges:
        print(edge)
