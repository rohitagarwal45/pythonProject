# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):

        if root is None:
            return 0

        ld = self.diameterOfBinaryTree(root.left)

        rd = self.diameterOfBinaryTree(root.right)

        f = self.height_of_tree(root.left) + self.height_of_tree(root.right) + 2
        return (max(f, max(ld, rd)))

    def height_of_tree(self, root):

        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        else:
            return max(self.height_of_tree(root.left), self.height_of_tree(root.right)) + 1



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
obj = Solution()
Q = obj.diameterOfBinaryTree(root)
print(Q)