# -*- coding: utf-8 -*-
"""
    @file: isBalancedTree.py
    @date: 2020-09-06 4:47 PM
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def maxHigh(root):
            if root == None:
                return 0
            return max(maxHigh(root.left), maxHigh(root.right)) + 1

        if root == None:
            return True

        return abs(maxHigh(root.left) - maxHigh(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)