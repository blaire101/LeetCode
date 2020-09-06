# -*- coding: utf-8 -*-
"""
    @file: maxDepth.py
    @date: 2020-09-06 5:27 PM
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
