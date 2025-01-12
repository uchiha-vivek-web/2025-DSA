class Node :
    def __init__(self,item=None,left=None,right=None):
        self.item = item
        self.left=left
        self.right=right
class BST :
    def __init__(self):
        self.root = None
    def insert(self,data):
        self.root = self.helper_insert(self.root,data)
    def helper_insert(self,root,data):
        if root is None :
            return Node(data)
        if data < root.item :
            root.left = self.helper_insert(root.left,data)
        elif data > root.item :
            root.right =self.helper_insert(root.right,data)
        return root
    def isChildrenSum(self,root):
        if root is None or (root.left is None and root.right is None):
            return 1
        sum  = 0
        if root.left is not None :
            sum+=root.left.data
        if root.right is not None :
            sum+=root.right.data
        return 1 if (root.data==sum and  self.isChildrenSum(root.left) and self.isChildrenSum(root.right)) else 0