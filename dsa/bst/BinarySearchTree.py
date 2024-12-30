class Node :
    def __init__(self,item=None,left=None,right=None):
        self.item = item
        self.left=left
        self.right = right
class BST : 
    def __init__(self):
        self.root = None
    def insert(self,data):
        self.root  = self.helper_insert(self.root,data)
    def helper_insert(self,root,data):
        if root is None:
            return Node(data)
        if data<root.item :
            root.left = self.helper_insert(root.left,data)
        elif data > root.item :
            root.right  = self.helper_insert(root.right,data)
        return root
    
    def search(self,data):
        return self.helper_search(self.root,data)
    def helper_search(self,root,data):
        if root is None or root.item==data:
            return root
        if data<root.item:
            return self.helper_search(root.left,data)
        else :
            return self.helper_search(root.right,data)


