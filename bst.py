class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
        return root

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                root.key = self._min_value_node(root.right)
                root.right = self._delete_recursive(root.right, root.key)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self._search_recursively(root.left, key)
        else:
            return self._search_recursively(root.right, key)

    def inorder_traversal(self):
        self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, root):
        if root:
            self._inorder_traversal_recursive(root.left)
            print(root.key, end=" ")
            self._inorder_traversal_recursive(root.right)


bst = BinarySearchTree()
bst.insert(100)
bst.insert(300)
bst.insert(200)
bst.insert(400)
bst.insert(900)
bst.insert(600)

print("Inorder traversal:",end=" ")
bst.inorder_traversal()
print()

bst.delete(200)
print("Inorder traversal after deleting 200:",end=" ")
bst.inorder_traversal()
print()

print("Is 30 in tree:", bst.search(500))
print("Is 100 in tree:", bst.search(100))
