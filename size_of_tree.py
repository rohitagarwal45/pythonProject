# 3.	Check if two trees are identical

class tree_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, child):
        if self.data == child.data:
            return
        # left sub tree
        if child.data < self.data:

            if self.left:
                self.left.add_child(child)
            else:
                self.left = child
        else:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = child

    def size_of_tree(node):
        if node == None:
            return  0
        else:
            return (tree_node.size_of_tree(node.left) + 1 + tree_node.size_of_tree(node.right))

def build_tree():
    list_a = [17, 4, 1, 20, 9, 23, 18, 34]
    root_node = tree_node(list_a[0])

    for i in range(1, len(list_a)):
        root_node.add_child(tree_node(list_a[i]))

    print(f"Size of tree is  : {tree_node.size_of_tree(root_node)}")


if __name__ == '__main__':
    build_tree()
