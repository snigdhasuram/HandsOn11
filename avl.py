class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def delete(self, root, key):
        if not root:
            return root

        elif key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def search(self, root, key):
        if root == None:
            return root,False

        if root.key == key:
            return root,True
        
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def preorder_traversal(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)


if __name__ == "__main__":
    avl_tree = AVLTree()
    root = None

    root = avl_tree.insert(root, 10)
    root = avl_tree.insert(root, 20)
    root = avl_tree.insert(root, 30)
    root = avl_tree.insert(root, 40)
    root = avl_tree.insert(root, 50)
    root = avl_tree.insert(root, 25)

    print("Preorder traversal after insertion:", end=" ")
    avl_tree.preorder_traversal(root)
    print()

    root = avl_tree.delete(root, 20)

    print("Preorder traversal after deleting 20:",end=" ")
    avl_tree.preorder_traversal(root)
    print()

    print("Is 25 in Tree:", avl_tree.search(root, 25)[1])
    print("Is 90 in Tree:", avl_tree.search(root, 90)[1])

