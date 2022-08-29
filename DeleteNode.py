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

    def inorder_predecessor(root):
        while root.right:
            root = root.right
        return root.val

    def inorder_successor(root):
        while root:
            root = root.left
        return root.val

    def deleteNode(self, root, key):

        if not root:
            return
        if key < root.val:
           root.left = self.deleteNode(root.left, key)
        elif key > root.val:
           root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right: #if node is last node
                return None
                # root.val = None

            elif root.left: # find inorder predecessor
                root.val = Solution.inorder_predecessor(root.left)
                root.left = self.deleteNode(root.left, root.val)
            else:# find inorder successor
                root.val = Solution.inorder_successor(root.right)
                root.right = self.deleteNode(root.right, root.val)




        # if not root:
        #     return
        # else:
        #     if root.val == key:
        #         #           delete the node and assign the rest
        #         if root.right:
        #             # root.val = root.right.val
        #             # root.right = None
        #             root.right.left = root.left
        #             root = root.right
        #
        #         elif root.left:
        #             # root.val = root.left.val
        #             # root.left = None
        #             root.left.right = root.right
        #             root = root.left
        #         else:
        #             del root.val
        #     elif root.val > key:
        #         # return self.deleteNode(root.left, key)
        #         self.deleteNode(root.left, key)
        #     elif root.right:
        #         # return self.deleteNode(root.right, key)
        #         self.deleteNode(root.right, key)
        #
        #     return root
        # list_node = []
        # if not root:
        #     return
        # else:
        #     if root.val == key:
        #         #           delete the node and assign the rest
        #         if root.right:
        #             root.val = root.right.val
        #             root.right = None
        #             # list_node.append(root.val)
        #             # list_node += root
        #         else:
        #             root.val = root.left.val
        #             root.left = None
        #             list_node.append(root.val)
        #             # return root
        #     elif root.val > key:
        #         # return self.deleteNode(root.left, key)
        #         list_node += self.deleteNode(root.left, key)
        #     else:
        #         # return self.deleteNode(root.right, key)
        #         list_node += self.deleteNode(root.right, key)
        #
        #     list_node.append(root.val)
        #     return list_node



def build_tree():
    # root = [5, 3, 6, 2, 4, None, 7]
    # root = [5,3,6,2,4,None,7]
    root = [5,3,6,2,4,None,7]
    # root = [0]
    print(f"type is {type(root)}")
    # key = 3
    # key = 0
    # key = 5
    key = 7

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
