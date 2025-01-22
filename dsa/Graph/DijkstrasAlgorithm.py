import heapq

def add_edge(graph,u,v,weight):
    if u not in graph :
        graph[u]=[]
    if v not in graph :
        graph[v] = []
    graph[u].append((v,weight))
    graph[v].append((u,weight))

def dijkstra(graph,start):
    pq=[] # priority queue
    distances = {node:float('inf') for node in graph }
    distances[start]=0
    # Push the start node with distance 0 to the queue
    heapq.heappush(pq,(0,start))
    while pq :
        # Pop the node with smallest distance
        current_distance,current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neigbor,weight in graph[current_node]:
            distance = current_distance + weight
            # if shorter distance is found
            if distance < distances[neigbor]:
                distances[neigbor]=distance
                heapq.heappush(pq,(distance,neigbor))
    return distances


if __name__ == "__main__":
    # Graph representation as an adjacency list
    graph = {}

    # Adding edges
    add_edge(graph, 'A', 'B', 1)
    add_edge(graph, 'A', 'C', 4)
    add_edge(graph, 'B', 'C', 2)
    add_edge(graph, 'B', 'D', 6)
    add_edge(graph, 'C', 'D', 3)

    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)

    print("Shortest distances from node", start_node, ":")
    for node, distance in shortest_distances.items():
        print(f"{node}: {distance}")

