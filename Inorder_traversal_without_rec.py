# Definition for a binary tree node.
# Inorder_traversal_without_rec.py
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        stack = []
        result = []
        if not root:
            return stack

        while True:

            if root:
                stack.append(root)
                root = root.left

            # result.append(root.val)

            elif stack:
                node = stack.pop()
                result.append(node.val)
                root = node.right
            else:
                break

        return result


root = TreeNode(1)
# root.left = TreeNode(2)
root.right = TreeNode(2)
# root.left.left = TreeNode(2)
root.right.left = TreeNode(3)
obj = Solution()
Q = obj.inorderTraversal(root)
print(Q)