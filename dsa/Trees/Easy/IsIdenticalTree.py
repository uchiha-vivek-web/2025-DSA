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

    @staticmethod
    def isIdentical(r1, r2) -> bool:
        # Base cases
        if r1 is None and r2 is None:
            return True
        if r1 is None or r2 is None:
            return False
        # Check current node and recurse for left and right subtrees
        return (
            r1.item == r2.item and
            BST.isIdentical(r1.left, r2.left) and
            BST.isIdentical(r1.right, r2.right)
        )

# Create two trees
tree1 = BST()
tree2 = BST()

tree1.insert(1)
tree1.insert(3)
tree1.insert(2)
tree1.insert(4)

tree2.insert(1)
tree2.insert(3)
tree2.insert(2)
tree2.insert(4)

# Check if the two trees are identical
ans = BST.isIdentical(tree1.root, tree2.root)
print(ans)
