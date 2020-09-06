# -*- coding: utf-8 -*-
"""
    @file: isSymmetric.py
    @date: 2020-09-06 5:31 PM
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetricHelper(left: TreeNode, right: TreeNode):
    if left == None and right == None:
        return True
    if left == None or right == None:
        return False
    if left.val != right.val:
        return False
    return isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left)


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        return root == None or isSymmetricHelper(root.left, root.right)