class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self._insert(root.left, data)
        elif data > root.item:
            root.right = self._insert(root.right, data)
        return root

    def isIdentical(self, a: Node, b: Node) -> bool:
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        return (
            a.item == b.item and
            self.isIdentical(a.left, b.left) and
            self.isIdentical(a.right, b.right)
        )

    def isSubtree(self, main: Node, sub: Node) -> bool:
        if main is None:
            return False
        if self.isIdentical(main, sub):
            return True
        return self.isSubtree(main.left, sub) or self.isSubtree(main.right, sub)

    


tree1 = BST()
tree2 = BST()

# tree1 = [3, 4, 5, 1, 2]
tree1.insert(3)
tree1.insert(4)
tree1.insert(5)
tree1.insert(1)
tree1.insert(2)

# tree2 = [4, 1, 2]
tree2.insert(4)
tree2.insert(1)
tree2.insert(2)

print(tree1.isSubtree(tree1.root, tree2.root))  # Output: True
