class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.helper_insert(self.root, data)

    def helper_insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.helper_insert(root.left, data)
        elif data > root.item:
            root.right = self.helper_insert(root.right, data)
        return root

    def isMirror(self, left, right):
        # Both subtrees are None -> Symmetric
        if left is None and right is None:
            return True
        # One subtree is None -> Not symmetric
        if left is None or right is None:
            return False
        # Check current nodes and their subtrees
        return (left.item == right.item) and \
               self.isMirror(left.left, right.right) and \
               self.isMirror(left.right, right.left)

    def isSymmetric(self):
        # A tree is symmetric if its left and right subtrees are mirrors
        if self.root is None:
            return True
        return self.isMirror(self.root.left, self.root.right)

# Example usage
tree = BST()
tree.insert(2)
tree.insert(1)
tree.insert(3)

print("Is the tree symmetric?", tree.isSymmetric())
