from collections import deque
class Graph :
    def __init__(self,vno):
        self.vertex_count = vno
        self.adj_list = {v : [] for v in range(vno)}
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v,weight))
        else :
            print('Invalid Vertices')
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count :
            self.adj_list[u] = [(vertex,weight) for vertex,weight in self.adj_list[u] if vertex !=v ]
        else :
            print('Invalid vertices')
    def print_adj_list(self):
        for vertex,neighbor in self.adj_list.items():
            print("V",vertex,":",neighbor)
    def bfs(self,start,X):
        if start <0 or start>= self.vertex_count:
            print('Invalid vertex count')
            return
        visited=[]
        queue= deque([start])
        while queue :
            pass