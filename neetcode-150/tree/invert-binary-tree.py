# create a BST
# Make all its instances
# time and space complexity of O(N)

from collections import deque

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
            root.right = self.helper_insert(root.right,data)
        return root

    def invert(self):
        if not self.root:
            return
        queue=deque([self.root])
        while queue:
            node = queue.popleft()
            node.left,node.right=  node.right,node.left
            print(node.item,end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()
    


if __name__ == "__main__":
    tree = BST()
    tree.insert(4)
    tree.insert(2)
    tree.insert(6)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    tree.insert(7)

    # tree.insert(1)
    # tree.insert(2)
    # tree.insert(3)
    # tree.insert(4)
    # tree.insert(5)
    # tree.insert(6)
    # tree.insert(7)
    tree.invert()