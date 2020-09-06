# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recur(root1, root2):
    if root2 is None:
        return True
    if root1 is None or root1.val != root2.val:
        return False
    return recur(root1.left, root2.left) and recur(root1.right, root2.right)


class Solution:

    def isSubStructure(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None or root2 is None:
            return False

        return recur(root1, root2) or \
               self.isSubStructure(root1.left, root2) or \
               self.isSubStructure(root1.right, root2)
