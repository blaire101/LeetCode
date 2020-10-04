# -*- coding: utf-8 -*-
"""
    @file: easy.mirrorTree.py
    @date: 2020-10-03 11:41 AM
    @desc:
    @url : https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/
"""


# Definition for a binary tree node.
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
