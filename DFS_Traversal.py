# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(root):  # need to return list

        q = []
        list_queue = []
        q1 = []
        if not root:
            return list_queue

        q.append(root)

        while len(q):
            # RPA Remove Print Add child Instead of print we need to append in queue
            node = q.pop(0)
            list_queue.append(node.val)

            if not len(q):
                q1.append(list(list_queue))
                list_queue.pop(0)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


        return q1 #list_queue
    # checking git hub


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

Q = Solution.levelOrder(root)
print(Q)