# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if q.val < p.val:
            dummy_node = p
            p = q
            q = dummy_node

        if root:
            if (p.val == root.val or q.val == root.val) or (p.val < root.val and q.val > root.val):
                return root
            elif p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)



