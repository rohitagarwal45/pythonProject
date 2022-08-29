class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

    # def add_child(self, child):
        
        # if self.val == child.val:
        #     return
        # # left sub tree
        # if child.val < self.val:
        #     if self.left:
        #         self.left.add_child(child)
        #     else:
        #         self.left = child
        # else:
        #     if self.right:
        #         self.right.add_child(child)
        #     else:
        #         self.right = child


class Solution(object):
    def max_depth(self, root):

        if not root:
            return 0
        #
        # if not root.left and not root.right:
        #     return 1
        # else:
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))


def build_tree():
    p = [3, 9, 20, None, None, 15, 7]
    root_p = TreeNode(p[0])

    root_p.left = TreeNode(9)
    root_p.right = TreeNode(20)
    root_p.right.left = TreeNode(15)
    root_p.right.right = TreeNode(7)

    # for i in range(1, len(p)):
    #     root_p.add_child(tree_node(p[i]))

    obj = Solution()
    print(obj.max_depth(root_p))


if __name__ == '__main__':
    build_tree()
