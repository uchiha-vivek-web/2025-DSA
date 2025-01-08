from collections import deque
def BFS(tree,start):
    visited=[]
    queue = deque([start])
    while queue :
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            print(node,end=' ')

            for neighbor in tree[node]:
                if neighbor not in visited:
                    queue.append(neighbor)



# Define the decision tree as a dictionary
tree = {
    # 'A': ['B', 'C'],  # Node A connects to B and C
    # 'B': ['D', 'E'],  # Node B connects to D and E
    # 'C': ['F', 'G'],  # Node C connects to F and G
    # 'D': ['H', 'I'],  # Node D connects to H and I
    # 'E': ['J', 'K'],  # Node E connects to J and K
    # 'F': ['L', 'M'],  # Node F connects to L and M
    # 'G': ['N', 'O'],  # Node G connects to N and O
    # 'H': [], 'I': [], 'J': [], 'K': [],  # Leaf nodes have no children
    # 'L': [], 'M': [], 'N': [], 'O': []   # Leaf nodes have no children
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    'D':['B','C','E','F'],
    'E':['C','D','F'],
    'F':['D','E']
}

BFS(tree,'A')