
# finding depth of the tree

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
            root.right =self.helper_insert(root.right,data)
        return root

    # height of binary tree
    def height_of_binary_tree(self,root):
        if root is None:
            return -1
        left_height = self.height_of_binary_tree(root.left)
        right_height = self.height_of_binary_tree(root.right)
        return max(left_height,right_height) + 1
    
    # calculate depth of specific node
    def depth_of_node(self,root,target,depth=0):
        if root is None:
            return -1
        
        if root.item==target:
            return depth
        
        elif target<root.item:
            return self.depth_of_node(root.left,target,depth+1)
        else:
            return self.depth_of_node(root.right,target,depth+1)
    
if __name__=="__main__":
    tree = BST()
    tree.insert(5)
    tree.insert(6)
    tree.insert(3)
    tree.insert(2)
    ans = tree.height_of_binary_tree(tree.root)
    ans1=tree.depth_of_node(tree.root,5)
    print(ans1)
    