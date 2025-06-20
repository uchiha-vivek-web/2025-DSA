from typing import Optional

# Node class
class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# BST class with insert and diameter logic
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
            root.right = self.helper_insert(root.right, data)  # Fixed: use '=' not '-'
        return root

    def diameter(self, root: Optional[Node]):
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            self.res = max(self.res, left + right)  # longest path through the node
            return 1 + max(left, right)

        dfs(root)
        return self.res

# Driver code
if __name__ == "__main__":
    tree = BST()
    tree.insert(5)
    tree.insert(3)
    tree.insert(2)
    tree.insert(4)
    tree.insert(8)
    tree.insert(7)
    tree.insert(9)

    print("Diameter of the tree:", tree.diameter(tree.root))
