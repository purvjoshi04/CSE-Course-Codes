import sys

def dijkstra(graph, start):
    # Initialize distances dictionary with start vertex having distance of 0
    distances = {vertex: sys.maxsize for vertex in graph}
    distances[start] = 0
    
    # Initialize set of visited vertices and unvisited vertices
    visited = set()
    unvisited = set(graph.keys())
    
    while unvisited:
        # Find the unvisited vertex with the smallest distance
        current = min(unvisited, key=lambda vertex: distances[vertex])
        
        # Stop if the smallest distance is infinity
        if distances[current] == sys.maxsize:
            break
        
        # Update distances for each neighbor of the current vertex
        for neighbor, weight in graph[current].items():
            if neighbor in visited:
                continue
            new_distance = distances[current] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
        
        # Mark current vertex as visited and remove from unvisited set
        visited.add(current)
        unvisited.remove(current)
    
    return distances

# User input for graph
graph = {}
num_vertices = int(input("Enter the number of vertices: "))
for i in range(num_vertices):
    vertex, *edges = input(f"Enter vertex and its neighbors with weights (in format 'vertex neighbor:weight ...') for vertex {i}: ").split()
    graph[vertex] = {}
    for edge in edges:
        neighbor, weight = edge.split(":")
        graph[vertex][neighbor] = int(weight)

# User input for starting vertex
start_vertex = input("Enter the starting vertex: ")

# Run Dijkstra's algorithm and print results
distances = dijkstra(graph, start_vertex)
print("Shortest distances from the starting vertex:")
for vertex, distance in distances.items():
    print(f"{vertex}: {distance}")
