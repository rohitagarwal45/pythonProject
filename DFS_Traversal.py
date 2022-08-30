# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(root):  # need to return list

        curr_q = []
        next_q = []
        result_q = []
        lev_q = []

        if not root:
            return curr_q

        curr_q.append(root)

        while len(curr_q):
            # RPA Remove Print Add child Instead of print we need to append in queue

            for i in range(len(curr_q)):
                node = curr_q.pop(0)
                lev_q.append(node.val)

                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)

            curr_q = next_q
            next_q = []
            result_q.append(lev_q)
            lev_q = []



        return result_q
    # checking git hub


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

Q = Solution.levelOrder(root)
print(Q)