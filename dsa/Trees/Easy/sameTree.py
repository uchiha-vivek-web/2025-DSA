# Node
class Node :
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
        

class BST :
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        self.root = self.helper_insert(self.root,data)
        
    
    def helper_insert(self,root,data):
        if root is None:
            return Node(data)
        
        if data < root.item :
            root.left = self.helper_insert(root.left,data)
        elif data > root.item :
            root.right = self.helper_insert(root.right,data)
        return root
      
      
      
def isSameTree(node1,node2):
    if node1 is None and node2 is None :
        return True
    if node1 is None or node2 is None :
        return False
      
    return (node1.item==node2.item  and 
        isSameTree(node1.left,node2.left) and isSameTree(node1.right,node2.right)
    )  
      
        

tree1=BST()
tree2=BST()


for value in [5,3,2,7,4,6,8]:
    tree1.insert(value)
    tree2.insert(value)
print(isSameTree(tree1.root,tree2.root))




