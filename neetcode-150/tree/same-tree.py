
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
    
    def isSameTree(self,p:Node,q:Node) -> bool :
        # Time complexity is O(N) --> N is number of nodes
        # Space complexity is O(h) --> h is the height of the tree

        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        return (   p.item==q.item and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
    

tree1 = BST()
tree2=BST()
tree1.insert(1)
tree1.insert(2)
tree1.insert(3)
tree2.insert(1)
tree2.insert(2)
tree2.insert(3)
ans= tree1.isSameTree(tree1.root,tree2.root)
print(ans)