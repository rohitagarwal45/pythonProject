# Definition for a binary tree node.
class TreeNode(object):
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


class Solution(object):
    def deleteNode(self, root, key):

        if not root:
            return
        else:
            if root.val == key:
                 #           delete the node and assign the rest
                if root.right:
                    root.val = root.right.val
                    root.right = None
                    return root
                else:
                    root.val = root.left.val
                    root.left = None
                    return root
            elif root.val > key:
                return self.deleteNode(root.left, key)
            else:
                return self.deleteNode(root.right, key)



def build_tree():
    root = [5, 3, 6, 2, 4, None, 7]
    key = 3

    root_node = TreeNode(root[0])

    # root_node.add_child(TreeNode(root[i])) if root[i] not None
    # else None
    for i in range(1, len(root)):
        if root[i]:
            root_node.add_child(TreeNode(root[i]))
        else:
            continue

    obj = Solution()
    return_node = obj.deleteNode(root_node, key)
    flag = 'X'


if __name__ == '__main__':
    build_tree()
