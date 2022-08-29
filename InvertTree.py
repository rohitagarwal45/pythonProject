# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add_child(self, child):
        if self.val == child.val:
            return

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

class Solution:
    def invertTree(self, root):

        if not root:  # if no node is there
            return
        if not root.left and not root.right:  # leaf node
            return
        else:
            lv_dummy = root.left
            root.left = root.right
            root.right = lv_dummy
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
            return root


def build_tree():
    root = [1]

    root_node = TreeNode(root[0])

    for i in range(1, len(root)):
        if root[i]:
            root_node.add_child(TreeNode(root[i]))
        else:
            continue

    obj = Solution()
    return_node = obj.invertTree(root_node)


if __name__ == '__main__':
    build_tree()




