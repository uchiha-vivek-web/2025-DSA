"""Bellman Ford Algorithm """
def add_edge(graph,u,v,weight):
    if u not in graph :
        graph[u] = []
    if v not in graph :
        graph[v] = []
    graph[u].append((v,weight))
    graph[v].append((u,weight))

def bellman_ford(graph,edges,start):
    distances = { node:float('inf')  for node in graph }
    distances[start]=0
    for _ in range(len(graph)-1):
        for u,v,weight in edges :
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u]+weight
    # check negative weight cycles
    for u,v,weight in edges :
        if distances[u] != float('inf') and  distances[u] + weight < distances[v]:
            raise ValueError('Graph contains neagtive wieght cycle')
    return distances

if __name__ == "__main__":
    # Graph representation as an adjacency list
    graph = {}
    edges = []

    # Adding edges
    add_edge(graph, 'A', 'B', 1)
    edges.append(('A', 'B', 1))
    add_edge(graph, 'A', 'C', 4)
    edges.append(('A', 'C', 4))
    add_edge(graph, 'B', 'C', 2)
    edges.append(('B', 'C', 2))
    add_edge(graph, 'B', 'D', 6)
    edges.append(('B', 'D', 6))
    add_edge(graph, 'C', 'D', 3)
    edges.append(('C', 'D', 3))

    start_node = 'A'
try:
        shortest_distances_bellman_ford = bellman_ford(graph, edges, start_node)
        print("\nBellman-Ford Algorithm - Shortest distances from node", start_node, ":")
        for node, distance in shortest_distances_bellman_ford.items():
            print(f"{node}: {distance}")
except ValueError as e:
        print("\n", e)