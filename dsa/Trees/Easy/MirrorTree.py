from collections import deque

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

    def mirror(self, root):
        if root is None:
            return
        # Inverting the right and left subtree
        self.mirror(root.left)
        self.mirror(root.right)

        # Swapping the left and right subtree
        root.left, root.right = root.right, root.left

    def bfs(self):
        if not self.root:
            print("Tree is empty")
            return

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.item, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Example usage
tree = BST()
tree.insert(1)
tree.insert(3)
tree.insert(2)
tree.insert(4)

print("BFS Traversal of the BST:")
tree.bfs()
print()
tree.mirror(tree.root)
tree.bfs()