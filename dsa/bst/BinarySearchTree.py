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

    def search(self, data):
        return self.helper_search(self.root, data)

    def helper_search(self, root, data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.helper_search(root.left, data)
        else:
            return self.helper_search(root.right, data)

    def inorder(self):
        result = []
        self.rinorder(self.root, result)
        return result

    def rinorder(self, root, result):
        if root:
            self.rinorder(root.left, result)
            result.append(root.item)
            self.rinorder(root.right, result)

    def preorder(self):
        result = []
        self.rpreorder(self.root, result)
        return result

    def rpreorder(self, root, result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left, result)
            self.rpreorder(root.right, result)

    def postorder(self):
        result = []
        self.rpostorder(self.root, result)
        return result

    def rpostorder(self, root, result):
        if root:
            self.rpostorder(root.left, result)
            self.rpostorder(root.right, result)
            result.append(root.item)

# Example Usage
tree = BST()
tree.insert(10)
tree.insert(30)
tree.insert(35)
tree.insert(40)

ans_inorder = tree.inorder()
ans_preorder = tree.preorder()
ans_postorder = tree.postorder()

print("Inorder:", ans_inorder)
print("Preorder:", ans_preorder)
print("Postorder:", ans_postorder)
