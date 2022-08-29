class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, child):
        if self.data == child.data:
            return
        # left subtree
        if self.data > child.data:
            if self.left:
                self.left.add_child(child)
            else:
                self.left = child
        # Right subtree
        else:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = child

    def inorder_travelsal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_travelsal()
            # elements += self.left.inorder_travelsal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_travelsal()
            # elements.append(self.right.inorder_travelsal())
        # elements.append(self.data)
        return elements

    def post_order_traversal(self):

        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)

        # if self.right:
        #     self.right.post_order_traversal()

        return elements

    def pre_order_traversal(self):

        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements


def build_tree(element):
    root = BST(element[0])
    for i in range(1, len(element)):
        root.add_child(BST(element[i]))
    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root_node = build_tree(numbers)
    # list_a =  list(root_node.inorder_travelsal())
    # print(f"incorder travalsal{list_a}")

    # list_post_order = root_node.post_order_traversal()
    # print(list_post_order)

    print(root_node.pre_order_traversal())
