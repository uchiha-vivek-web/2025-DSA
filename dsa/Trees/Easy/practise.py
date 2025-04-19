

class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right

class BST :
    def __init__(self):
        self.root=None
    def insert(self,data):
        self.root  =self.helper_insert(self.root,data)
    
    def helper_insert(self,root,data):
        if root is None :
            return Node(data)
        if data < root.item:
            root.left = self.helper_insert(root.left,data)
        elif data>root.item:
            root.right = self.helper_insert(root.right,data)
        return root
    def height(self,root):
        if root is None :
            return -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return max(left_height,right_height)+1
    

if __name__=="__main__":
    tree=BST()
    tree.insert(10)
    tree.insert(30)
    tree.insert(35)
    tree.insert(40)
    ans=tree.height(tree.root)
    print(ans)