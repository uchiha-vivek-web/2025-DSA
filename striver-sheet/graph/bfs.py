"""  BFS of graph   """
from collections import deque

class Graph :
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_list = { v : [] for v in range(vno)}
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))
        else:
            print('Invalid vertices')

    def print_adj_list(self):
        for vertex,neighbors in self.adj_list.items():
            print(f'V {vertex} : {neighbors} ')

    def bfs(self,start):
        if start<0 or start >= self.vertex_count:
            print('Invalid start vertex')
            return
        
        visited=[]
        queue = deque([start])

        while queue :
            node = queue.popleft()
            if node not in visited :
                visited.append(node)
                print(node,end=' ')

                for neighbor,_ in self.adj_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

# Example Usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.print_adj_list()

print("BFS Traversal:")
g.bfs(0)
