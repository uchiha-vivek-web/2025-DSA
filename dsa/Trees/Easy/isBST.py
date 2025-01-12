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

    def inorder(self):
        result = []
        self.helper_inorder(self.root, result)
        return result

    def helper_inorder(self, root, result):
        if root:
            self.helper_inorder(root.left, result)
            result.append(root.item)
            self.helper_inorder(root.right, result)

    """ Finding max value in the subtree rooted at the given node """
    def max_subtree(self, root):
        if root is None:
            return float('-inf')
        if isinstance(root, int):
            root = self.find_node(self.root, root)
        if root is None:
            return float('-inf')
        return max(root.item, self.max_subtree(root.left), self.max_subtree(root.right))

    def find_node(self, current, value):
        if current is None or current.item == value:
            return current
        if value < current.item:
            return self.find_node(current.left, value)
        return self.find_node(current.right, value)

# Example Usage
tree = BST()
tree.insert(2)
tree.insert(1)
tree.insert(3)

ans = tree.inorder()
print("Inorder Traversal:", ans)

max_subtree_value = tree.max_subtree(2)
print("Max Value in Subtree rooted at 2:", max_subtree_value)
