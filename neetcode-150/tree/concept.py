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

    def height(self, root):
        if root is None:
            return -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return max(left_height, right_height) + 1

    # BFS - Level Order Traversal
    def bfs(self):
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.item, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

    # DFS - Preorder Traversal
    def dfs_preorder(self, node):
        if node:
            print(node.item, end=" ")
            self.dfs_preorder(node.left)
            self.dfs_preorder(node.right)

    # DFS - Inorder Traversal
    def dfs_inorder(self, node):
        if node:
            self.dfs_inorder(node.left)
            print(node.item, end=" ")
            self.dfs_inorder(node.right)

    # DFS - Postorder Traversal
    def dfs_postorder(self, node):
        if node:
            self.dfs_postorder(node.left)
            self.dfs_postorder(node.right)
            print(node.item, end=" ")

if __name__ == "__main__":
    tree = BST()
    tree.insert(10)
    tree.insert(8)
    tree.insert(12)
    tree.insert(14)

    print("Height of tree:", tree.height(tree.root))

    print("BFS (Level Order):")
    tree.bfs()

    print("DFS Preorder:")
    tree.dfs_preorder(tree.root)
    print()

    print("DFS Inorder:")
    tree.dfs_inorder(tree.root)
    print()

    print("DFS Postorder:")
    tree.dfs_postorder(tree.root)
    print()
