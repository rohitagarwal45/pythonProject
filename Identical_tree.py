class tree_node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

    def add_child(self, child):
        if self.val == child.val:
            return
        # left sub tree
        if child.val < self.val:
            if self.left:
                self.left.add_child(child)
            else:
                self.left = child
        else:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = child


class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


def build_tree():
    p = [1, 2, 3]
    q = [1, 2, 3]
    root_p = tree_node(p[0])
    root_q = tree_node(q[0])

    for i in range(1, len(p)):
        root_p.add_child(tree_node(p[i]))

    for j in range(1, len(q)):
        root_q.add_child(tree_node(q[j]))

    obj = Solution()
    print(obj.isSameTree(root_p, root_q))

if __name__ == '__main__':
    build_tree()
