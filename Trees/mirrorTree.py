# -*- coding: utf-8 -*-
"""
    @file: mirrorTree.py
    @date: 2020-09-06 5:56 PM
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root

        node = root.left
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(node)

        return root

