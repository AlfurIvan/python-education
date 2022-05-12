"""module Binary Search Tree implementation"""
from random import randint


class BinaryTreeNode:
    """node for binary tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        """fill left leaf"""
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        """fill right leaf"""
        self.right = BinaryTreeNode(value)
        return self.right


class BinarySearchTree:
    """class for tree"""
    searching_result = None
    previous_s_node = None

    def __init__(self, value):
        self.root = BinaryTreeNode(value)

    def insert(self, value):
        """insert item"""
        new_leaf = BinaryTreeNode(value)
        carriage_root = self.root
        success_flag = False

        while not success_flag:
            if value < carriage_root.value:
                if carriage_root.left is None:
                    carriage_root.left = new_leaf
                    success_flag = True

                else:
                    carriage_root = carriage_root.left
            else:
                if carriage_root.right is None:
                    carriage_root.right = new_leaf
                    success_flag = True

                else:
                    carriage_root = carriage_root.right

    def lookup(self, value):
        """find node by value"""
        if value is None:
            return False
        else:
            self.search(value, self.root)
            return self.searching_result

    def search(self, value, carriage_root):
        """lookup helper"""
        if value == carriage_root.value:
            self.searching_result = carriage_root
            return
        elif value < carriage_root.value:
            if carriage_root.left is not None:
                self.previous_s_node = carriage_root
                self.search(value, carriage_root.left)
        elif value >= carriage_root.value:
            if carriage_root.right is not None:
                self.previous_s_node = carriage_root
                self.search(value, carriage_root.right)

    def delete(self, value):
        """delete item by value"""
        if value is None:
            return
        if not isinstance(self.lookup(value), BinaryTreeNode):
            raise Exception
        else:
            l_snippet, r_snippet = self.searching_result.left, self.searching_result.right
            if self.searching_result.value < self.previous_s_node.value:
                self.previous_s_node.left = None
            else:
                self.previous_s_node.right = None
            self.rebuilder(l_snippet)
            self.rebuilder(r_snippet)

    def rebuilder(self, node_to_rewrite):
        """rebuild tree after deletion"""
        if node_to_rewrite is not None:
            l_snippet, r_snippet = node_to_rewrite.left, node_to_rewrite.right
            self.insert(node_to_rewrite.value)
            self.rebuilder(l_snippet)
            self.rebuilder(r_snippet)
        else:
            return

    def printer(self):
        """printer"""
        self.pre_order(self.root)

    def pre_order(self, node):
        """recursive helper for printer"""
        if node:
            print(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)


if __name__ == "__main__":

    tree = BinarySearchTree(32)
    data = ...
    print(32)
    for leaf in range(8):
        data = randint(20, 50)
        print(data)
        tree.insert(data)

    print('\n\nThe tree:')
    tree.printer()

    tree.delete(None)
    print('\n\nAfter del None')
    tree.printer()
    print("What do you want to delete?: ")
    to_del = int(input())
    tree.delete(to_del)
    print(f'\n\nAfter del {to_del}')
    tree.printer()

    print("What do you want to delete?: ")
    to_del = int(input())
    tree.delete(to_del)
    print(f'\n\nAfter del wrong {to_del}')
    tree.printer()
