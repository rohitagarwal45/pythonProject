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
    def binaryTreePaths(self, root):

        list1 = []

        def dfs(root, path):
            if not root:
                return
            if not root.left and not root.right:
                path += str(root.val)
                list1.append(path)
                return
            else:
                path += str(root.val) + "->"
            dfs(root.left, path)
            dfs(root.right, path)

        dfs(root, "")
        return list1




                # if root.left:
                #     # str1 += (str(root.val) + '->' + str(self.binaryTreePaths(root.left)))
                #     str1 = "".join([str(root.val), '->', str(self.binaryTreePaths(root.left))])
                #     list1.append(str1)
                #     return str1
                # if root.right:
                #     str2 = "".join([str(root.val), '->', str(self.binaryTreePaths(root.right))])
                #     list1.append(str2)
                #     return str2
                # return (if root.left :
                #             "".join([str(root.val), '->', str(self.binaryTreePaths(root.left))])
                #         if root.right:
                #             "".join([str(root.val), '->', str(self.binaryTreePaths(root.right))]) ))


def build_tree():
    root = [10, 5, 11, None, 8]

    root_node = TreeNode(root[0])

    for i in range(1, len(root)):
        if root[i]:
            root_node.add_child(TreeNode(root[i]))
        else:
            continue

    obj = Solution()
    return_node = obj.binaryTreePaths(root_node)
    print(return_node)


if __name__ == '__main__':
    build_tree()
