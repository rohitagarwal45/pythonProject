# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):

        if root is None:
            return

        curr_q = []
        next_q = []
        level_q = []
        result_q = []

        curr_q.append(root)
        count = 1

        while curr_q:

            for i in range(len(curr_q)):
                node = curr_q.pop(len(curr_q) - 1 )
                level_q.append(node.val)

                if count % 2 != 0:  # even no then right to left
                    if node.right:
                        next_q.append(node.right)
                    if node.left:
                        next_q.append(node.left)
                else:  # left to right
                    if node.left:
                        next_q.append(node.left)
                    if node.right:
                        next_q.append(node.right)

            count += 1

            level_q.reverse()
            result_q.append(level_q)
            curr_q = next_q
            next_q = []
            level_q = []

        return result_q


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
obj = Solution()
Q = obj.zigzagLevelOrder(root)
print(Q)
