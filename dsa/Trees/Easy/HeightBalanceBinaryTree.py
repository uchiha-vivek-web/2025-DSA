"""Height Balance binary Tree"""
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
        if root is None :
            return Node(data)
        if data < root.item :
            root.left = self.helper_insert(root.left,data)
        elif data>root.item :
            root.right = self.helper_insert(root.right,data)
        return root
    def height(self,root) -> int :
        if root is None :
            return -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return max(left_height,right_height)+1
    def isBalanced(self,root)->bool :
        if root is None :
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)
        if (abs(lh-rh) <=1) and self.isBalanced(root.left) is True and self.isBalanced(root.right) is True :
            return True
        return False
tree  = BST()
tree.insert(2)
tree.insert(1)
tree.insert(3)
ans = tree.isBalanced(tree.root)
print(ans)