from collections import deque
from typing import List
class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right


class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        self.root = self.helper_insert(self.root,data)

    
    def helper_insert(self,root,data):
        if root is None:
            return Node(data)
        
        if data<root.item:
            root.left = self.helper_insert(root.left,data)
        elif data>root.item:
            root.right=self.helper_insert(root.right,data)
        return root
    
    #BFS tRAVERSAL --> root node provided
    def bfs(self):
        if not self.root:
            return
        
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.item,end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

    def levelOrder(self, root: Node) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(current_level)
        
        return result
    

    def dfslvl(self,root:Node):
        res=[]
        def dfs(node,depth):
            if not node:
                return None
            if len(res)==depth:
                res.append([])
            
            res[depth].append(node.val)
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        
        dfs(root,0)
        return res


if __name__=="__main__":
    tree = BST()
    tree.insert(4)
    tree.insert(2)
    tree.insert(5)
    # print('BFS Traversal')
    # tree.bfs()
    print('DFS Traversal')
    tree.dfslvl(tree.root())