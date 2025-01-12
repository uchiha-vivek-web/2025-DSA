from collections import deque
def BFS(tree,start):
    visited= []
    queue = deque([start])
    while queue :
        node  = queue.popleft()
        if node  not in visited :
            visited.append(node)
            print(node,end=' ')
            for neighbor in tree[node]:
                if neighbor not in visited :
                    queue.append(neighbor)

tree = {
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    'D':['B','C','E','F'],
    'E':['C','D','F'],
    'F':['D','E']
}
BFS(tree,'A')