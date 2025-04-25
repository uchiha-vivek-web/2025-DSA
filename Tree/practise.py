class Node :
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
    

class BST :
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        self.root= self.helper_insert(self.root,data)

    def  helper_insert(self,root,data):
        if root is None:
            return Node(data)
        
        if data<root.item:
            self.left = self.helper_insert(root.left,data)
        elif data>root.item:
            self.right=self.helper_insert(root)
        