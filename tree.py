class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret   


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def find_min_node(node):
    if node is None:
        return None
    
    while node.left:
        node = node.left
    return node.val


def find_max_node(node):
    if node is None:
        return None
    
    while node.right:
        node = node.right
    return node.val


def sum_all_nodes(node):
    if node is None:
        return 0    
    
    sum = node.val + sum_all_nodes(node.left) + sum_all_nodes(node.right)

    return sum
