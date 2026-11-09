from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)
            
    def search(self, value):
        current_node = self.root

        while current_node is not None:
            if value == current_node.value:
                return current_node

            elif value < current_node.value:
                current_node = current_node.left

            else:
                current_node = current_node.right

        return None
            
class AVLTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def height(self, node):
        if node is None:
            return 0

        return 1 + max(
            self.height(node.left),
            self.height(node.right)
        )

    def balance_factor(self, node):
        if node is None:
            return 0

        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, node):
        new_root = node.right
        temp = new_root.left

        new_root.left = node
        node.right = temp

        return new_root

    def right_rotate(self, node):
        new_root = node.left
        temp = new_root.right

        new_root.right = node
        node.left = temp

        return new_root

    def rebalance(self, node):
        balance = self.balance_factor(node)

        # Левое поддерево слишком высокое
        if balance > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.left_rotate(node.left)

            return self.right_rotate(node)

        # Правое поддерево слишком высокое
        if balance < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.right_rotate(node.right)

            return self.left_rotate(node)

        return node

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        return self.rebalance(node)
            
def bfs(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
def dfs_preorder(node):
    if node:
        print(node.value, end=' ')
        dfs_preorder(node.left)
        dfs_preorder(node.right)

def dfs_inorder(node):
    if node:
        dfs_inorder(node.left)
        print(node.value, end=' ')
        dfs_inorder(node.right)

def dfs_postorder(node):
    if node:
        dfs_postorder(node.left)
        dfs_postorder(node.right)
        print(node.value, end=' ')

tree = BinaryTree()

tree.insert(5)
tree.insert(10)
tree.insert(2)
tree.insert(3)
tree.insert(6)

tree.inorder(tree.root)
print('')
bfs(tree.root)
print('')
dfs_preorder(tree.root)
print('')
dfs_inorder(tree.root)
print('')
dfs_postorder(tree.root)
print('')

tree_2 = AVLTree()

tree_2.insert(5)
tree_2.insert(10)
tree_2.insert(2)
tree_2.insert(3)
tree_2.insert(6)

tree_2.inorder(tree_2.root)
print()

bfs(tree_2.root)